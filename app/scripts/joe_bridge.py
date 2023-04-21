from time import sleep
from logzero import logger
from web3 import Web3

from app.helpers.utils import approve, call_function, get_random_amount, wait_balance_after_bridge, wait_balance_is_changed_token
import config


def joe_bridge(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    srcToken = srcChain.get(params.get("srcToken"))

    srcTokenAddress = w3.toChecksumAddress(srcToken.get("address"))

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dstToken = dstChain.get(params.get("dstToken"))
    w3_dst = Web3(Web3.HTTPProvider(dstChain.get("RPC")))
    dst_token_contract = w3_dst.eth.contract(
        address=w3_dst.toChecksumAddress(dstToken["address"]),
        abi=config.TOKEN_ABI,
    )
    dstBalanceBefore = dst_token_contract.functions.balanceOf(wallet.address).call()

    gas_multiplier = srcChain.get("GAS_MULTIPLIER")
    oft_contract = w3.eth.contract(
        address=srcTokenAddress,
        abi=config.TOKEN_ABI,
    )

    tryNum = 0
    approve_result = False
    while True:
        try:
            # amount in
            balance_wei = oft_contract.functions.balanceOf(wallet.address).call()
            random_amount = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))
            decimals_balance = w3.fromWei(random_amount, srcToken.get("decimals"))
            str_balance_splitted = str(decimals_balance).split(".")
            formatted_decimals = str_balance_splitted[1] if len(str_balance_splitted[1]) == 18 else str_balance_splitted[1] + "0" * (18 - len(str_balance_splitted[1]))
            amount_to_bridge_8_decimals = float(f"{str_balance_splitted[0]}.{formatted_decimals[:8]}")
            amount_to_bridge_8_decimals_wei = w3.toWei(amount_to_bridge_8_decimals, config.ETH_DECIMALS)

            if params.get("srcChain") == "AVALANCHE":
                proxy = srcChain.get("JOE_PROXY")
                proxy_address = w3.toChecksumAddress(proxy.get("address"))
                if approve_result == False:
                    logger.info("Approving ...")
                    approve_result = approve(w3, oft_contract, proxy_address, amount_to_bridge_8_decimals_wei, wallet)
                    sleep(3)
                oft_contract = w3.eth.contract(
                    address=proxy.get("address"),
                    abi=config.TOKEN_ABI,
                )

            logger.info("Bridging ...")
            sliced_wallet_address = wallet.address[2:]
            adapter_params = srcChain["LZ_ADAPTER_PARAMS"] + sliced_wallet_address
            bridgeParams = (
                wallet.address,
                dstChain.get("LZ_CHAIN_ID"),
                config.PREFIX_TO_BYTES_ADDRESS + sliced_wallet_address,
                amount_to_bridge_8_decimals_wei,
                amount_to_bridge_8_decimals_wei,
                (wallet.address, config.ZERO_ADDRESS, adapter_params)
            )
            sendFee = oft_contract.functions.estimateSendFee(
                dstChain.get("LZ_CHAIN_ID"), wallet.address, amount_to_bridge_8_decimals_wei, False, adapter_params).call()[0]
            value = w3.fromWei(sendFee, config.ETH_DECIMALS)
            call_function(oft_contract.functions.sendFrom, wallet, w3, value=value,
                    args=bridgeParams, gas_multiplicator=gas_multiplier)
            if config.WAIT_BALANCE:
                wait_balance_is_changed_token(dst_token_contract, wallet.address, dstBalanceBefore)
            return True

        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while bridging - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while bridging.\n{e}")
                return False
            sleep(10)

