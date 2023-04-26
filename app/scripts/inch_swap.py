import random
from time import sleep

from web3 import Web3
from logzero import logger
from app.helpers.utils import get_random_amount, send_raw_transaction, get

import config


def inch_swap(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    srcChainId = srcChain.get("CHAIN_ID")
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    srcToken = srcChain.get(params.get("srcToken"))
    srcTokenAddress = w3.toChecksumAddress(srcToken.get("address")) if params.get("srcToken") != "ETH" else config.ETH_INCH

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dstToken = dstChain.get(params.get("dstToken"))
    dstTokenAddress = w3.toChecksumAddress(dstToken.get("address")) if params.get("dstToken") != "ETH" else config.ETH_INCH

    logger.info("INFO | 1inch | Swapping ...")
    approved = False
    tryNum = 0
    slippage = config.SWAP_SLIPPAGE

    while True:

        if srcTokenAddress == config.ETH or srcTokenAddress == config.ETH_INCH:
            balance_wei = w3.eth.get_balance(wallet.address)
        else:
            token = w3.eth.contract(
                address=srcTokenAddress,
                abi=config.TOKEN_ABI,
            )
            balance_wei = token.functions.balanceOf(wallet.address).call()

        amount_in_wei = int(balance_wei / 100 * get_random_amount(params["amountPercentMin"], params["amountPercentMax"], 2, 3))


        if srcTokenAddress != config.ETH and srcTokenAddress.lower() != config.ETH_INCH.lower() and approved == False:
            approved = approve(w3, wallet, srcTokenAddress, srcChainId, amount_in_wei)

        swap_url_api = f'https://api.1inch.io/v4.0/{srcChainId}/swap?fromTokenAddress={srcTokenAddress}&toTokenAddress={dstTokenAddress}' \
                       f'&amount={amount_in_wei}&fromAddress={wallet.address}&slippage={slippage}'
        # try:
        json_data = get(swap_url_api)
        tx = json_data.json().get('tx')
        tx['nonce'] = w3.eth.getTransactionCount(wallet.address)
        tx['to'] = w3.toChecksumAddress(tx['to'])
        tx['gasPrice'] = int(tx['gasPrice'])
        tx['value'] = int(tx['value'])
        signed_tx = wallet.sign_transaction(tx)
        receipt = send_raw_transaction(w3, signed_tx)
        logger.info(f'INFO | 1inch | Successfully swaped {srcTokenAddress} => {dstTokenAddress}')
        sleep(random.randint(random.randint(5, 6), random.randint(7, 8)))
        return receipt
        # except Exception as e:
        #     tryNum += 1
        #     slippage += 1
        #     logger.error((f"ERROR | 1inch | Swap attempt {tryNum}. Can't swap {srcTokenAddress} => {dstTokenAddress}"))
        #     logger.error(f"Tryed with url {swap_url_api}")
        #     if tryNum > config.ATTEMTS_TO_API_REQUEST:
        #         if "'NoneType' object does not support item assignment" in e.args[0]:
        #             e = "Can't get estimated data from 1inch"
        #         logger.error((f"ERROR | 1inch | Can't swap {srcTokenAddress} => {dstTokenAddress}\n {e}"))
        #         return False
        #     sleep(10)

def approve(w3, wallet, srcAddress, chainId, amountIn):
    logger.info("INFO | 1inch | Calling approve ...")
    tryNum = 0

    while True:
        try:
            _1inchurl = f'https://api.1inch.io/v4.0/{chainId}/approve/transaction?tokenAddress={srcAddress}&amount={amountIn}'
            json_data = get(_1inchurl).json()

            tx = {
                "nonce": w3.eth.getTransactionCount(wallet.address),
                "to": w3.toChecksumAddress(json_data["to"]),
                "data": json_data["data"],
                "gasPrice": w3.eth.gas_price,
                "gas": w3.eth.estimate_gas({
                    'to': w3.toChecksumAddress(wallet.address),
                    'from': w3.toChecksumAddress(wallet.address),
                    'value': w3.toWei(0.0001, 'ether')
                }) + random.randint(100000, 120000),
            }

            signed_txn = wallet.sign_transaction(tx)
            receipt = send_raw_transaction(w3, signed_txn)
            logger.info(f'INFO | 1inch | Successful approved')
            return receipt
        except Exception as error:
            tryNum += 1
            logger.error(f'ERROR | 1inch | An error occured while approving on 1inch.\n{error}')
            if tryNum > config.ATTEMTS_TO_API_REQUEST:
                logger.error((f"ERROR | 1inch | Can't approve {srcAddress} \n {error}"))
                return False
            sleep(15)
