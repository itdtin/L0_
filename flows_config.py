from config import *
# Flows
PROJECTS = {
   "stargateUSDC" : [
        #1) USDC(arb) - USDC(Polygon) - USDT(BSC) - USDC(BASE) - USDC(arb)
        {
            "script": "stargate_stable_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "POLYGON",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 5.9,
            "gasOnDestinationMax": 5.95
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "POLYGON",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDT",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.009,
            "gasOnDestinationMax": 0.0091
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "BSC",
            "dstChain": "BASE",
            "srcToken": "USDT",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.0007,
            "gasOnDestinationMax": 0.0009
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "BASE",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        }
    ],
    "stargateETH" : [
        # {
        #     "script": "stargate_eth_bridge",
        #     "srcChain": "ARBITRUM",
        #     "dstChain": "LINEA",
        #     "amountPercentMin": 100,
        #     "amountPercentMax": 100,
        # },
        {
            "script": "stargate_eth_bridge",
            "srcChain": "LINEA",
            "dstChain": "BASE",
            "amountPercentMin": 99,
            "amountPercentMax": 99,
        },
        # {
        #     "script": "stargate_eth_bridge",
        #     "srcChain": "BASE",
        #     "dstChain": "ARBITRUM",
        #     "amountPercentMin": 100,
        #     "amountPercentMax": 100,
        # },
    ]
}
