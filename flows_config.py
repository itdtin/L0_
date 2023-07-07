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
            "amountPercentMin": 45,
            "amountPercentMax": 56,
        },
        {
            "script": "oft_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "OPTIMISM",
            "srcToken": "BTCB",
            "dstToken": "BTCB",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.001,
            "gasOnDestinationMax": 0.0015
        },
        {
            "script": "oft_bridge",
            "srcChain": "OPTIMISM",
            "dstChain": "ARBITRUM",
            "srcToken": "BTCB",
            "dstToken": "BTCB",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
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

    "traderjoe": [
        {
            "script": "trader_joe_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "JOE",
            "amountPercentMin": 40,
            "amountPercentMax": 65,
        },
        {
            "script": "joe_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "BSC",
            "srcToken": "JOE",
            "dstToken": "JOE",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.01,
            "gasOnDestinationMax": 0.015
        },
        {
            "script": "joe_bridge",
            "srcChain": "BSC",
            "dstChain": "ARBITRUM",
            "srcToken": "JOE",
            "dstToken": "JOE",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
        {
            "script": "trader_joe_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "JOE",
            "dstToken": "ETH",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
        },
    ],
    "stargate1" : [
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
            "dstChain": "OPTIMISM",
            "srcToken": "ETH",
            "dstToken": "ETH",
            "amountMin": 0.001,
            "amountMax": 0.0014, # 0.0024 is max on bungee from ARM to OPTIMISM
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "OPTIMISM",
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
            "dstChain": "POLYGON",
            "srcToken": "ETH",
            "dstToken": "MATIC",
            "amountMin": 0.0014,
            "amountMax": 0.0015, # 0.0524 is max on bungee from ARB to POLYGON
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "OPTIMISM",
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
            "dstChain": "AVALANCHE",
            "srcToken": "ETH",
            "dstToken": "AVAX",
            "amountMin": 0.001,
            "amountMax": 0.00139, # 0.0139 is max on bungee from ARM to AVALANCHE
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "POLYGON",
            "dstChain": "AVALANCHE",
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
            "srcChain": "AVALANCHE",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDT",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "BSC",
            "dstChain": "ARBITRUM",
            "srcToken": "USDT",
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
    "stargate2" : [
        # 2) USDC(arb) - USDC(pol) - USDC(ava) - USDC(arb)
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
            "amountMin": 0.001,
            "amountMax": 0.00139, # 0.0139 is max on bungee from ARM to BSC
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "POLYGON",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0, #вопрос
            "gasOnDestinationMax": 0
        },
        {
            "script": "bungee_refuel",
            "srcChain": "ARBITRUM",
            "dstChain": "AVALANCHE",
            "srcToken": "ETH",
            "dstToken": "AVAX",
            "amountMin": 0.001,
            "amountMax": 0.00139, # 0.0139 is max on bungee from ARM to BSC
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "POLYGON",
            "dstChain": "AVALANCHE",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0
        },
        {
            "script": "stargate_stable_bridge",
            "srcChain": "AVALANCHE",
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
    ]
}
