from _typeshed import Incomplete
from typing import Any

class Comment:
    content: Incomplete
    author: Incomplete
    height: Incomplete
    width: Incomplete
    def __init__(self, text, author, height: int = 79, width: int = 144) -> None: ...
    @property
    def parent(self) -> Any: ...  # AnyOf[Cell, MergedCell, ReadOnlyCell]
    def __eq__(self, other: Comment) -> bool: ...  # type: ignore[override]
    def __copy__(self): ...
    def bind(self, cell) -> None: ...
    def unbind(self) -> None: ...
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
