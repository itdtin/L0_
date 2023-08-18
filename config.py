import dotenv
from app.helpers.abis import TOKEN_ABI, JOE_ROUTER_ABI, STARGATE_ROUTER_ABI, REFUEL_ABI
from eth_utils.units import units, decimal

units.update(
    {
        "4_dec": decimal.Decimal("10000"),  # # Add in 4 decimals
        "8_dec": decimal.Decimal("100000000"),  # Add in 8 decimals
    }
)

dotenv.load_dotenv()
to_run = {
    "bitcoinBridge": {
        "swap": False,
        "bridge": False
    },
    "traderjoe": {
        "swap": False,
        "bridge": False
    },
    "stargate1": {
        "swap": True,
        "refuel": True,
        "bridge": True
    },
    "stargate2": {
        "swap": True,
        "refuel": True,
        "bridge": True
    }
}
to_random_run = list(to_run.keys())

# Wait
WAIT_BTW_WALLET_MIN: int = 1
WAIT_BTW_WALLET_MAX: int = 2

WAIT_BTW_PROJECT_MIN: int = 3
WAIT_BTW_PROJECT_MAX: int = 4

WAIT_RECEIPT = [(4,5), (7,8)]

BRIDGE_BALANCE_WAIT_TIME: int = 20000 # 20000 seconds


ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9

SWAP_SLIPPAGE: int = 5

# Tokens
ZERO_ADDRESS: str = "0x0000000000000000000000000000000000000000"
ETH_INCH: str = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ETH: str = "0x0000000000000000000000000000000000000000"
ETH_DECIMALS: str = "ether"
USDC_DECIMALS: str = "mwei"
BTCB_DECIMALS: str = "8_dec"

#Bungee addresses
REFUEL_ARBITRUM: str = "0xc0e02aa55d10e38855e13b64a8e1387a04681a00"
REFUEL_OPTIMISM: str = "0x5800249621DA520aDFdCa16da20d8A5Fc0f814d8"
REFUEL_POLYGON: str = "0xAC313d7491910516E06FBfC2A0b5BB49bb072D91"
REFUEL_AVALANCHE: str = "0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB"
REFUEL_BSC: str = "0xBE51D38547992293c89CC589105784ab60b004A9"
REFUEL_FANTOM: str = "0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB"

# Networks
ARBITRUM_RPC: str = "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
ARBITRUM_CHAIN_ID: int = 42161
ARBITRUM_LZ_CHAIN_ID: int = 110

OPTIMISM_RPC: str = "https://opt-mainnet.g.alchemy.com/v2/0K6bMED4RlCn2DPr8tKQS8XTRMcUDKFR"
OPTIMISM_CHAIN_ID: int = 10
OPTIMISM_LZ_CHAIN_ID: int = 111

POLYGON_RPC: str = "https://polygon-mainnet.g.alchemy.com/v2/ncSSy-j4i1T3hcN5hFCtEsyghpLCw_0p"
POLYGON_CHAIN_ID: int = 137
POLYGON_LZ_CHAIN_ID: int = 109

AVALANCHE_RPC: str = "https://avalanche-mainnet.infura.io/v3/ca0d7f3c70f84e22ab29e5a74b329a3a"
AVALNCHE_CHAIN_ID: int = 43114
AVALANCHE_LZ_CHAIN_ID: int = 106

BSC_RPC: str = "https://bsc-dataseed4.binance.org"
BSC_CHAIN_ID: int = 56
BSC_LZ_CHAIN_ID: int = 102

FANTOM_RPC: str = "https://rpc.ankr.com/fantom"
FANTOM_CHAIN_ID: int = 250
FANTOM_LZ_CHAIN_ID: int = 112

#Protocols
ARBITRUB_JOE_SWAP_CONTRACT: str = "0xb4315e873dbcf96ffd0acd8ea43f689d8c20fb30"
PREFIX_TO_BYTES_ADDRESS: str = "0x000000000000000000000000"

STARGATER_ROUTER_OPTI: str = "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b"
STARGATE_ROUTER_ARBI: str = "0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614"
STARGATE_ROUTER_POLYGON: str = "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd"
STARGATE_ROUTER_FANTOM: str = "0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6"
STARGATER_ROUTER_AVALANCHE: str = "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd"
STARGATE_ROUTER_BSC: str = "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8"

NETWORKS = {
    "ARBITRUM": {
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": ARBITRUM_CHAIN_ID,
        "LZ_CHAIN_ID": ARBITRUM_LZ_CHAIN_ID,
        "RPC": ARBITRUM_RPC,
        "LZ_ADAPTER_PARAMS": "0x0002000000000000000000000000000000000000000000000000000000000003d0900000000000000000000000000000000000000000000000000000000000000000",
        "JOE_ROUTER_ADDRESS": ARBITRUB_JOE_SWAP_CONTRACT,
        "STARGATE_ROUTER_ADDRESS": STARGATE_ROUTER_ARBI,
        "REFUEL_ADDRESS": REFUEL_ARBITRUM,
        "USDC": {
            "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
            "decimals": USDC_DECIMALS
        },
        "BTCB": {
            "address": "0x2297aEbD383787A160DD0d9F71508148769342E3",
            "decimals": BTCB_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "WETH": {
            "address": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
            "decimals": ETH_DECIMALS
        },
        "JOE": {
            "address": "0x371c7ec6D8039ff7933a2AA28EB827Ffe1F52f07",
            "decimals": ETH_DECIMALS
        }
    },
    "POLYGON": {
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": POLYGON_CHAIN_ID,
        "LZ_CHAIN_ID": POLYGON_LZ_CHAIN_ID,
        "RPC": POLYGON_RPC,
        "STARGATE_ROUTER_ADDRESS": STARGATE_ROUTER_POLYGON,
        "REFUEL_ADDRESS": REFUEL_POLYGON,
        "USDC": {
            "address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0x55d398326f99059ff775485246999027b3197955",
            "decimals": ETH_DECIMALS
        }
    },
    "OPTIMISM": {
        "GAS_MULTIPLIER": 6,
        "CHAIN_ID": OPTIMISM_CHAIN_ID,
        "LZ_CHAIN_ID": OPTIMISM_LZ_CHAIN_ID,
        "RPC": OPTIMISM_RPC,
        "STARGATE_ROUTER_ADDRESS": STARGATER_ROUTER_OPTI,
        "REFUEL_ADDRESS": REFUEL_OPTIMISM,
        "LZ_ADAPTER_PARAMS": "0x000200000000000000000000000000000000000000000000000000000000002dc6c00000000000000000000000000000000000000000000000000000000000000000",
        "USDC": {
            "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",
            "decimals": ETH_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "BTCB": {
            "address": "0x2297aEbD383787A160DD0d9F71508148769342E3",
            "decimals": BTCB_DECIMALS
        }
    },
    "BSC": {
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": BSC_CHAIN_ID,
        "LZ_CHAIN_ID": BSC_LZ_CHAIN_ID,
        "RPC": BSC_RPC,
        "LZ_ADAPTER_PARAMS": "0x0002000000000000000000000000000000000000000000000000000000000030d4000000000000000000000000000000000000000000000000000000000000000000",
        "STARGATE_ROUTER_ADDRESS": STARGATE_ROUTER_BSC,
        "REFUEL_ADDRESS": REFUEL_BSC,
        "BNB": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "JOE": {
            "address": "0x371c7ec6D8039ff7933a2AA28EB827Ffe1F52f07",
            "decimals": ETH_DECIMALS
        },
        "USDT": {
            "address": "0x55d398326f99059ff775485246999027b3197955",
            "decimals": ETH_DECIMALS
        }
    },
    "AVALANCHE": {
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": AVALNCHE_CHAIN_ID,
        "LZ_CHAIN_ID": AVALANCHE_LZ_CHAIN_ID,
        "RPC": AVALANCHE_RPC,
        "STARGATE_ROUTER_ADDRESS": STARGATER_ROUTER_AVALANCHE,
        "REFUEL_ADDRESS": REFUEL_AVALANCHE,
        "LZ_ADAPTER_PARAMS": "0x0002000000000000000000000000000000000000000000000000000000000003d0900000000000000000000000000000000000000000000000000000000000000000",
        "AVAX": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "JOE_PROXY": {
            "address": "0x371c7ec6D8039ff7933a2AA28EB827Ffe1F52f07",
            "decimals": ETH_DECIMALS
        },
        "JOE": {
            "address": "0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd",
            "decimals": ETH_DECIMALS
        },
        "USDC": {
            "address": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
            "decimals": USDC_DECIMALS
        }
    },
    "FANTOM": {
        "GAS_MULTIPLIER": 6,
        "CHAIN_ID": FANTOM_CHAIN_ID,
        "LZ_CHAIN_ID": FANTOM_LZ_CHAIN_ID,
        "RPC": FANTOM_RPC,
        "STARGATE_ROUTER_ADDRESS": STARGATE_ROUTER_FANTOM,
        "REFUEL_ADDRESS": REFUEL_FANTOM,
        "USDC": {
            "address": "0x04068DA6C83AFCFA0e13ba15A6696662335D5B75",
            "decimals": USDC_DECIMALS
        }
    },
}
swap_params = {
    "trader_joe_swap": {
        "BTCB": {
            "swap_in": {
                "pairBinSteps": [10],
                "versions": [2]
            },
            "swap_out": {
                "pairBinSteps": [10],
                "versions": [2]
            }
        },
        "JOE": {
            "swap_in": {
                "pairBinSteps": [20],
                "versions": [1]
            },
            "swap_out": {
                "pairBinSteps": [0],
                "versions": [0]
            }
        }
    }
}
