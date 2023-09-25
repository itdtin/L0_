import random
from time import sleep

from web3 import Web3
from logzero import logger
from app.helpers.utils import call_function, get_random_amount, wait_balance_is_changed_ETH

import config

gas = 2_000_000

def stargate_eth_bridge(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    gas_multiplier = srcChain["GAS_ETH_MULTIPLIER"]

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dst_lz_chain_id = dstChain.get("LZ_CHAIN_ID")
    w3_dst = Web3(Web3.HTTPProvider(dstChain.get("RPC")))
    dst_router_address = w3.toChecksumAddress(dstChain.get("STARGATE_ETH_ROUTER_ADDRESS"))
    dstBalanceBefore = w3_dst.eth.getBalance(wallet.address)

    tryNum = 0
    while True:
        try:
            logger.info("Bridging ...")
            src_router = w3.eth.contract(address=srcChain.get("STARGATE_ETH_ROUTER_ADDRESS"), abi=config.STARGATE_ETH_ROUTER_ABI)
            src_fee_quoter = w3.eth.contract(address=srcChain.get("STARGATE_ROUTER_ADDRESS"), abi=config.STARGATE_ROUTER_ABI)
            balance_wei = w3.eth.get_balance(wallet.address)
            random_amount = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))
            stargate_fee = src_fee_quoter.functions.quoteLayerZeroFee(
                                dst_lz_chain_id, 1, wallet.address, "0x", (0, 0, wallet.address)).call()[0]
            gas = w3.eth.estimate_gas(
                {
                    "to": Web3.toChecksumAddress(src_router.address),
                    "from": Web3.toChecksumAddress(wallet.address),
                    "value": w3.toWei(0.0001, "ether"),
                }
            ) + random.randint(50000, 100000)
            gas_wei = int(gas * gas_multiplier * w3.eth.gas_price)

            swapObj = {
                '_dstChainId': dst_lz_chain_id,
                "_refundAddress": w3.toChecksumAddress(wallet.address),
                "_toAddress": w3.toChecksumAddress(wallet.address),
                "_amountLD": random_amount - stargate_fee - gas_wei,
                "_minAmountLD": int((random_amount - stargate_fee - gas_wei) * 0.95),
            }

            receipt = call_function(
                src_router.functions.swapETH,
                wallet,
                w3,
                args=swapObj.values(),
                value=w3.fromWei(random_amount, config.ETH_DECIMALS),
                gas_multiplicator=gas_multiplier,
                gas=gas
            )
            if receipt:
                wait_balance_is_changed_ETH(w3_dst, wallet.address, dstBalanceBefore)
            return True
        except TimeoutError as e:
            logger.error(f"ERROR | Didn't receive income ")
            return False
        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while swapping - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while swapping.\n{e}")
                return False
            sleep(10)
