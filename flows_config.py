from config import *
# Flows
PROJECTS = {
   "stargateUSDC" : [
        #1) USDC(arb) - USDC(opt) - USDC(pol) - USDC(ava) - USDT(bsc) - USDC(arb)
        { #swap for this project turned off in config.py
            "script": "inch_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "USDC",
            "amountPercentMin": 75, # 75%
            "amountPercentMax": 83,
        },
        {
            "script": "bungee_refuel",
            "srcChain": "ARBITRUM",
            "dstChain": "POLYGON",
            "srcToken": "ETH",
            "dstToken": "MATIC",
            "amountMin": 0.0014,
            "amountMax": 0.0015, # 0.0524 is max on bungee from ARB to POLYGON
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "POLYGON",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
        {
            "script": "bungee_refuel",
            "srcChain": "ARBITRUM",
            "dstChain": "BSC",
            "srcToken": "ETH",
            "dstToken": "BNB",
            "amountMin": 0.001,
            "amountMax": 0.00139, # 0.0139 is max on bungee from ARM to BSC
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "POLYGON",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDT",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
        {
            "script": "bungee_refuel",
            "srcChain": "ARBITRUM",
            "dstChain": "BASE",
            "srcToken": "ETH",
            "dstToken": "ETH",
            "amountMin": 0.001,
            "amountMax": 0.00139, # 0.0139 is max on bungee from ARM to AVALANCHE
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "BSC",
            "dstChain": "BASE",
            "srcToken": "USDT",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
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
        },
        { #swap for this project turned off in config.py
            "script": "inch_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "ETH",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
        },
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
