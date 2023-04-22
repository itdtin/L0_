from time import sleep

from web3 import Web3
from logzero import logger
from app.helpers.utils import approve, call_function, get_random_amount, wait_balance_is_changed_token

import config

srcPoolId = 1
dstPoolId = 1
gas = 3_000_000



def stargate_usdc_bridge(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    srcToken = srcChain.get(params.get("srcToken"))
    srcTokenAddress = w3.toChecksumAddress(srcToken.get("address"))
    gas_multiplier = srcChain.get("GAS_MULTIPLIER")

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dst_lz_chain_id = dstChain.get("LZ_CHAIN_ID")
    dstToken = dstChain.get(params.get("dstToken"))
    dst_router_address = w3.toChecksumAddress(dstChain.get("STARGATE_ROUTER_ADDRESS"))
    w3_dst = Web3(Web3.HTTPProvider(dstChain.get("RPC")))
    dst_token_contract = w3_dst.eth.contract(
        address=w3_dst.toChecksumAddress(dstToken["address"]),
        abi=config.TOKEN_ABI,
    )
    dstBalanceBefore = dst_token_contract.functions.balanceOf(wallet.address).call()

    approve_result = False
    tryNum = 0
    while True:
        try:
            logger.info("Bridging ...")
            src_router = w3.eth.contract(address=srcChain.get("STARGATE_ROUTER_ADDRESS"), abi=config.STARGATE_ROUTER_ABI)

            src_token_contract = w3.eth.contract(address=srcTokenAddress, abi=config.TOKEN_ABI)

            balance_wei = src_token_contract.functions.balanceOf(wallet.address).call()
            random_amount = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))

            if not approve_result:
                approve_result = approve(w3, src_token_contract, src_router.address, random_amount, wallet)
            # eth_balance = w3.eth.getBalance(wallet.address)
            # try:
            #     feeForWithWholeETHDrop = src_router.functions.quoteLayerZeroFee(
            #         dst_lz_chain_id, 1, dst_router_address, "0x", (0, eth_balance, wallet.address)).call()
            # except Exception as e:
            #     logger.error(f"To low ETH balance to drop ...{e}")
            #     feeForWithWholeETHDrop = src_router.functions.quoteLayerZeroFee(
            #         dst_lz_chain_id, 1, dst_router_address, "0x", (0, 0, wallet.address)).call()

            # gas_ = int(gas * w3.eth.gas_price)
            # fee = w3.fromWei(feeForWithWholeETHDrop[0] - eth_balance + gas_, config.ETH_DECIMALS)
            # eth_balance_to_drop_wei = eth_balance - w3.toWei(float(fee) * config.stg_nominator, config.ETH_DECIMALS)
            # if eth_balance_to_drop_wei > 0:
            #     value = float(fee) + float(w3.fromWei(eth_balance_to_drop_wei, config.ETH_DECIMALS))
            gas_on_destination_amount = params.get("gasOnDestination")
            if gas_on_destination_amount > 0:
                gas_on_dst_wei = w3.toWei(gas_on_destination_amount, config.ETH_DECIMALS)
            stargate_fee = src_router.functions.quoteLayerZeroFee(
                    dst_lz_chain_id, 1, dst_router_address, "0x", (0, gas_on_dst_wei, wallet.address)).call()[0]

            swapObj = {
                '_dstChainId': dst_lz_chain_id,
                "_srcPoolId": srcPoolId,
                "_dstPoolId": dstPoolId,
                "_refundAddress": w3.toChecksumAddress(wallet.address),
                "_amountLD": random_amount,
                "_minAmountLD": int(random_amount * 0.95),
                "_lzTxParams": (0, gas_on_dst_wei, w3.toChecksumAddress(wallet.address)),
                "_to": w3.toChecksumAddress(wallet.address),
                "_payload": "0x"
            }

            call_function(
                src_router.functions.swap,
                wallet,
                w3,
                args=swapObj.values(),
                value=w3.fromWei(stargate_fee, config.ETH_DECIMALS),
                gas_multiplicator=gas_multiplier
            )
            if config.WAIT_BALANCE:
                wait_balance_is_changed_token(dst_token_contract, wallet.address, dstBalanceBefore)
            return True
        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while swapping - attempt {tryNum}.\n{e}")
            if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                logger.error(f"ERROR | while swapping.\n{e}")
                return False
            sleep(10)
