from config import *
# Flows
PROJECTS = {
    "bitcoinBridge": [
        {
            "script": "trader_joe_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "BTCB",
            "amountPercentMin": 92, # 92%
            "amountPercentMax": 92,
        },
        # {
        #     "script": "bitcoinbridge",
        #     "srcChain": "ARBITRUM",
        #     "dstChain": "OPTIMISM",
        #     "srcToken": "BTCB",
        #     "dstToken": "BTCB",
        #     "amountPercentMin": 100,
        #     "amountPercentMax": 100
        # },
        # {
        #     "script": "bitcoinbridge",
        #     "srcChain": "OPTIMISM",
        #     "dstChain": "ARBITRUM",
        #     "srcToken": "BTCB",
        #     "dstToken": "BTCB",
        #     "amountPercentMin": 100,
        #     "amountPercentMax": 100
        # },
        {
            "script": "trader_joe_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "BTCB",
            "dstToken": "ETH",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
        },
    ],

}
