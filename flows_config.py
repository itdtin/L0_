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
            "amountPercentMin": 70, # 70%
            "amountPercentMax": 73,
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
            "amountPercentMin": 70,
            "amountPercentMax": 75,
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
    "stargate" : [
        {
            "script": "inch_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "USDC",
            "amountPercentMin": 70, # 50%
            "amountPercentMax": 73,
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "POLYGON",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 5,
            "gasOnDestinationMax": 7
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "POLYGON",
            "dstChain": "OPTIMISM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.001,
            "gasOnDestinationMax": 0.0015
        },
        {
            "script": "inch_swap",
            "srcChain": "OPTIMISM",
            "dstChain": "OPTIMISM",
            "srcToken": "USDC",
            "dstToken": "ETH",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
        },
        # stargate2
        {
            "script": "inch_swap",
            "srcChain": "OPTIMISM",
            "dstChain": "OPTIMISM",
            "srcToken": "ETH",
            "dstToken": "USDC",
            "amountPercentMin": 75, # 50%
            "amountPercentMax": 80,
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "OPTIMISM",
            "dstChain": "AVALANCHE",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.3,
            "gasOnDestinationMax": 0.33
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "AVALANCHE",
            "dstChain": "FANTOM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 8,
            "gasOnDestinationMax": 9
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "FANTOM",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.001,
            "gasOnDestinationMax": 0.0013
        },
        {
            "script": "inch_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "ETH",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
        },
    ],
}
