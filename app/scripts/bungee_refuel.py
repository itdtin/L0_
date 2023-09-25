from time import sleep
from logzero import logger
from web3 import Web3

from app.helpers.utils import call_function, get_random_amount, wait_balance_is_changed_ETH
import config


def bungee_refuel(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3_src = Web3(Web3.HTTPProvider(srcChain.get("RPC")))

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    w3_dst = Web3(Web3.HTTPProvider(dstChain.get("RPC")))

    dstBalanceBefore = w3_dst.eth.get_balance(wallet.address)

    gas_multiplier = srcChain.get("GAS_MULTIPLIER")
    refuel_contract = w3_src.eth.contract(
        address=w3_src.toChecksumAddress(srcChain.get("REFUEL_ADDRESS")),
        abi=config.REFUEL_ABI,
    )

    tryNum = 0
    while True:
        try:
            random_amount = get_random_amount(params["amountMin"], params["amountMax"], 15, 18)

            logger.info("Refueling GAS...")
            refuelParams = (
                dstChain.get("CHAIN_ID"),
                wallet.address
            )

            value = random_amount
            call_function(refuel_contract.functions.depositNativeToken, wallet, w3_src, value=value,
                    args=refuelParams, gas_multiplicator=gas_multiplier)
            if config.BRIDGE_BALANCE_WAIT_TIME:
                wait_balance_is_changed_ETH(w3_dst, wallet.address, dstBalanceBefore)
            return True

        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while bridging - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while bridging.\n{e}")
                return False
            sleep(10)

