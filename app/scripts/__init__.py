from app.scripts.oft_bridge import oft_bridge
from app.scripts.joe_bridge import joe_bridge
from app.scripts.trader_joe_swap import trader_joe_swap



__all__ = [
    trader_joe_swap,
    oft_bridge,
    joe_bridge
]


def scripts():
    return __all__
