from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatch

@_dispatch
def cycle_basis(G, root: Incomplete | None = None): ...
@_dispatch
def simple_cycles(G, length_bound: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...

class _NeighborhoodCache(dict[Incomplete, Incomplete]):
    G: Incomplete
    def __init__(self, G) -> None: ...
    def __missing__(self, v): ...

@_dispatch
def chordless_cycles(G, length_bound: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
@_dispatch
def recursive_simple_cycles(G): ...
@_dispatch
def find_cycle(G, source: Incomplete | None = None, orientation: Incomplete | None = None): ...
@_dispatch
def minimum_cycle_basis(G, weight: Incomplete | None = None): ...
