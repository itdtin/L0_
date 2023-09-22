from app.scripts.oft_bridge import oft_bridge
from app.scripts.joe_bridge import joe_bridge
from app.scripts.trader_joe_swap import trader_joe_swap
from app.scripts.inch_swap import inch_swap
from app.scripts.stargate_stable_bridge import stargate_stable_bridge
from app.scripts.stargate_eth_bridge import stargate_eth_bridge
from app.scripts.bungee_refuel import bungee_refuel




__all__ = [
    trader_joe_swap,
    oft_bridge,
    joe_bridge,
    inch_swap,
    stargate_stable_bridge,
    bungee_refuel,
    stargate_eth_bridge
]


def scripts():
    return __all__
