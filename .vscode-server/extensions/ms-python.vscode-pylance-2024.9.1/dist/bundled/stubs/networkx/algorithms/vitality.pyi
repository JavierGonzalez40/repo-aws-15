from functools import partial
from typing import Any

from ..classes.graph import Graph

__all__ = ["closeness_vitality"]

def closeness_vitality(G: Graph, node: Any = None, weight: str | None = None, wiener_index=None) -> dict | float: ...
