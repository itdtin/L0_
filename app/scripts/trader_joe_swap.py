from time import sleep
from logzero import logger
from web3 import Web3

from app.helpers.utils import approve, call_function, get_price, get_random_amount, max_int
import config

def trader_joe_swap(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    srcToken = srcChain.get(params.get("srcToken"))
    srcTokenAddress = w3.toChecksumAddress(srcToken.get("address"))
    src_decimals = srcToken.get("decimals")

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dstToken = dstChain.get(params.get("dstToken"))
    dstTokenAddress = w3.toChecksumAddress(dstToken.get("address"))
    dst_decimals = dstToken.get("decimals")

    gas_multiplier = srcChain.get("GAS_MULTIPLIER")
    weth_address = w3.toChecksumAddress(srcChain.get("WETH").get("address"))
    router_address = w3.toChecksumAddress(srcChain.get("JOE_ROUTER_ADDRESS"))
    joe_swap_router = w3.eth.contract(
        address=router_address,
        abi=config.JOE_ROUTER_ABI
    )

    approve_result = False
    tryNum = 0
    while True:
        try:
            if srcTokenAddress == config.ETH:
                balance_wei = w3.eth.get_balance(wallet.address)
                src_symbol = "ETH"
                swap_params = "swap_in"
            else:
                swap_params = "swap_out"
                token = w3.eth.contract(
                    address=srcTokenAddress,
                    abi=config.TOKEN_ABI,
                )
                src_symbol = token.functions.symbol().call().split(".")[0] # in case to get BTC.b price
                balance_wei = token.functions.balanceOf(wallet.address).call()

            if dstTokenAddress == config.ETH:
                dst_symbol = "ETH"
            else:
                dst_token_contract = w3.eth.contract(
                    address=dstTokenAddress,
                    abi=config.TOKEN_ABI,
                )
                dst_symbol = dst_token_contract.functions.symbol().call().split(".")[0] # in case to get BTC.b price

            # amount in
            src_token_price = get_price(src_symbol)
            if params.get("srcToken") == "JOE":
                random_amount = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))
                decimals_balance = w3.fromWei(random_amount, srcToken.get("decimals"))
                str_balance_splitted = str(decimals_balance).split(".")
                formatted_decimals = str_balance_splitted[1] if len(str_balance_splitted[1]) == 18 else str_balance_splitted[1] + "0" * (18 - len(str_balance_splitted[1]))
                amount_to_bridge_8_decimals = float(f"{str_balance_splitted[0]}.{formatted_decimals[:8]}")
                amount_in_wei = w3.toWei(amount_to_bridge_8_decimals, config.ETH_DECIMALS)
            else:
                amount_in_wei = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))
            amount_in_float = w3.fromWei(amount_in_wei, src_decimals)
            amount_in_usd = float(amount_in_float) * src_token_price

            # amount out min
            btc_price = get_price(dst_symbol)
            amount_out_min_usd = amount_in_usd / btc_price / 100 * (100 - config.SWAP_SLIPPAGE)
            amount_out_min_wei = w3.toWei(amount_out_min_usd, dst_decimals)
            sleep(3)

            # path params
            path_params = None
            for key, value in config.swap_params["trader_joe_swap"].items():
                if src_symbol in key or dst_symbol in key:
                    path_params = value[swap_params]
            if srcTokenAddress != config.ETH and approve_result == False:
                logger.info("Approving ...")
                approve_result = approve(w3, token, router_address, amount_in_wei, wallet)
                sleep(3)
            logger.info("Swapping ...")
            gas_multiplier += 1
            deadline = max_int
            if srcTokenAddress == config.ETH:
                swapParams = (
                    amount_out_min_wei,
                    (path_params["pairBinSteps"], path_params["versions"], [weth_address, dstTokenAddress]),
                    wallet.address,
                    deadline
                )
                call_function(joe_swap_router.functions.swapExactNATIVEForTokens, wallet, w3, value=amount_in_float,
                        args=swapParams, gas_multiplicator=gas_multiplier)
            else:
                swapParams = (
                    amount_in_wei,
                    amount_out_min_wei,
                    (path_params["pairBinSteps"], path_params["versions"], [srcTokenAddress, weth_address]),
                    wallet.address,
                    deadline
                )
                call_function(joe_swap_router.functions.swapExactTokensForNATIVE, wallet, w3, value=0,
                            args=swapParams, gas_multiplicator=gas_multiplier)
            return True

        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while swapping - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while swapping.\n{e}")
                return False
            sleep(10)
