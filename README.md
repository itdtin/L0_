# L0_worker
# Developed by [BenderRoyman](https://t.me/BenderRoyman)

# Prerequisites:
  Python 3.9
  wallets.txt in the root with primary keys line by line

# Install
  Be sure that the "python" command runs python 3.9
  1. Create virtual environment: python -m venv venv
  2. Activate venv: source venv/bin/activate - unix, venv\scripts\activate - windows
  3. Install dependencies: pip install -r requirements.txt

## Configure run:
  ### config.py - there are several parts which you would need to configure:
      #### select run:
        to_run = {
        "bitcoinBridge": {
            "swap": True,
            "bridge": True
        },
        ...
      }  - if you would like to not run any bridge or swap - you can set False,
    #### Wait time between wallets:
      WAIT_BTW_WALLET_MIN: int = 20
      WAIT_BTW_WALLET_MAX: int = 30
      Final wait time between wallets will be random amount in seconds in range from WAIT_BTW_WALLET_MIN to WAIT_BTW_WALLET_MAX
    #### Wait time between run scripts bridge or swap:
      WAIT_BTW_PROJECT_MIN: int = 30
      WAIT_BTW_PROJECT_MAX: int = 40
      Final wait time between run scripts will be random amount in seconds in range from WAIT_BTW_WALLET_MIN to WAIT_BTW_WALLET_MAX
    - Wait time balance on the destination chain:
      BRIDGE_BALANCE_WAIT_TIME: int = 3600 # 3600 seconds
      Script will wait receiving funds on the destination chain
  ### flows_config.py - there are configs for each flow and you would want to change something, look at the exapmple below:

    PROJECTS = {
      "bitcoinBridge": [
          {
              "script": "trader_joe_swap", - what script used to execute swap/bridge
              "srcChain": "ARBITRUM", - source chain for swap/bridge
              "dstChain": "ARBITRUM", - destination chain for swap/bridge
              (in case of swap both source and destination chains must be the same)

              "srcToken": "ETH", - source token for swap/bridge
              "dstToken": "BTCB", - destination token for swap/bridge
              "amountPercentMin": 45, - min percent of the balance to use for amount
              "amountPercentMax": 56, - max percent of the balance to use for amount
          },
          {
              "script": "oft_bridge",
              "srcChain": "ARBITRUM",
              "dstChain": "OPTIMISM",
              "srcToken": "BTCB",
              "dstToken": "BTCB",
              "amountPercentMin": 100,
              "amountPercentMax": 100,
              "gasOnDestinationMin": 0.002, - min amount to drop to destination chain, measured in the destination currency
              "gasOnDestinationMax": 0.0025 - max amount to drop to destination chain, measured in the destination currency
          },
          ...
      ],
      ...
    }

# Run
  python main_flow.py
