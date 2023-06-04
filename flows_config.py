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
            "gasOnDestinationMin": 0.002,
            "gasOnDestinationMax": 0.0025
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
    "stargate" : [
        {
            "script": "inch_swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "USDC",
            "amountPercentMin": 75, # 75%
            "amountPercentMax": 83,
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "OPTIMISM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.004,
            "gasOnDestinationMax": 0.0045
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "OPTIMISM",
            "dstChain": "AVALANCHE",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0.25,
            "gasOnDestinationMax": 0.3
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "AVALANCHE",
            "dstChain": "POLYGON",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 1.3,
            "gasOnDestinationMax": 2
        },
        {
            "script": "stargate_usdc_bridge",
            "srcChain": "POLYGON",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountPercentMin": 100,
            "amountPercentMax": 100,
            "gasOnDestinationMin": 0,
            "gasOnDestinationMax": 0

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
    ]
}
