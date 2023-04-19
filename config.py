import dotenv
from app.helpers.abis import TOKEN_ABI, JOE_ROUTER_ABI
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
        "swap": True,
        "bridge": True
    },
    "POLYGON": {
        "swap": True,
        "bridge": True
    },
    "OPTIMISM": {
        "swap": True,
        "bridge": True
    },
}

ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9
BRIDGE_BALANCE_WAIT_TIME: int = 2000 # 2000 seconds

SWAP_SLIPPAGE: int = 5
# Wait
WAIT_BTW_WALLET_MIN: int = 0
WAIT_BTW_WALLET_MAX: int = 0

WAIT_BTW_PROJECT_MIN: int = 0
WAIT_BTW_PROJECT_MAX: int = 0

# Tokens
ETH: str = "0x0000000000000000000000000000000000000000"
ETH_DECIMALS: str = "ether"
USDC_DECIMALS: str = "mwei"
BTCB_DECIMALS: str = "8_dec"

# Networks
ARBITRUM_RPC: str = "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
ARBITRUM_CHAIN_ID: int = 42161

OPTIMISM_RPC: str = "https://opt-mainnet.g.alchemy.com/v2/0K6bMED4RlCn2DPr8tKQS8XTRMcUDKFR"
OPTIMISM_CHAIN_ID: int = 10

POLYGON_RPC: str = "https://polygon-mainnet.g.alchemy.com/v2/ncSSy-j4i1T3hcN5hFCtEsyghpLCw_0p"
POLYGON_CHAIN_ID: int = 56

ARBITRUB_JOE_SWAP_CONTRACT: str = "0xb4315e873dbcf96ffd0acd8ea43f689d8c20fb30"

NETWORKS = {
    "ARBITRUM": {
        "GAS_LEFT": 4,
        "GAS_MULTIPLIER": 4,
        "CHAIN_ID": ARBITRUM_CHAIN_ID,
        "RPC": ARBITRUM_RPC,
        "JOE_ROUTER_ADDRESS": ARBITRUB_JOE_SWAP_CONTRACT,
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
        }
    },
    "POLYGON": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 1,
        "CHAIN_ID": POLYGON_CHAIN_ID,
        "RPC": POLYGON_RPC,
        "USDC": {
            "address": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0x55d398326f99059ff775485246999027b3197955",
            "decimals": ETH_DECIMALS
        }
    },
    "OPTIMISM": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 4,
        "CHAIN_ID": OPTIMISM_CHAIN_ID,
        "RPC": OPTIMISM_RPC,
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
}
