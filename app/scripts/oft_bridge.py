from time import sleep
from logzero import logger
from web3 import Web3

from app.helpers.utils import call_function, get_random_amount, wait_balance_after_bridge
import config


def oft_bridge(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    srcToken = srcChain.get(params.get("srcToken"))
    srcTokenAddress = w3.toChecksumAddress(srcToken.get("address"))

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dstToken = dstChain.get(params.get("dstToken"))

    gas_multiplier = srcChain.get("GAS_MULTIPLIER")
    btcb_contract = w3.eth.contract(
        address=srcTokenAddress,
        abi=config.TOKEN_ABI,
    )

    tryNum = 0
    while True:
        try:
            balance_wei = btcb_contract.functions.balanceOf(wallet.address).call()
            # amount in
            amount_in_wei = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))

            logger.info("Bridging ...")
            sliced_wallet_address = wallet.address[2:]
            adapter_params = srcChain["LZ_ADAPTER_PARAMS"] + sliced_wallet_address
            bridgeParams = (
                wallet.address,
                dstChain.get("LZ_CHAIN_ID"),
                config.PREFIX_TO_BYTES_ADDRESS + sliced_wallet_address,
                amount_in_wei,
                amount_in_wei,
                (wallet.address, config.ZERO_ADDRESS, adapter_params)
            )
            sendFee = btcb_contract.functions.estimateSendFee(
                dstChain.get("LZ_CHAIN_ID"), wallet.address, amount_in_wei, False, adapter_params).call()[0]
            value = w3.fromWei(sendFee, config.ETH_DECIMALS)
            call_function(btcb_contract.functions.sendFrom, wallet, w3, value=value,
                    args=bridgeParams, gas_multiplicator=gas_multiplier)
            if config.WAIT_BALANCE:
                wait_balance_after_bridge(wallet.address, dstToken, dstChain)
            return True

        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while bridging - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while bridging.\n{e}")
                return False
            sleep(10)

