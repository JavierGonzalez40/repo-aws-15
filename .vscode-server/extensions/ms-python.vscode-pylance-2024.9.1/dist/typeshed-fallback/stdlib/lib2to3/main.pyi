from _typeshed import FileDescriptorOrPath
from collections.abc import Container, Iterable, Iterator, Mapping, Sequence
from logging import _ExcInfoType
from typing import AnyStr, Literal

from . import refactor as refactor

def diff_texts(a: str, b: str, filename: str) -> Iterator[str]: ...

class StdoutRefactoringTool(refactor.MultiprocessRefactoringTool):
    nobackups: bool
    show_diffs: bool
    def __init__(
        self,
        fixers: Iterable[str],
        options: Mapping[str, object] | None,
        explicit: Container[str] | None,
        nobackups: bool,
        show_diffs: bool,
        input_base_dir: str = "",
        output_dir: str = "",
        append_suffix: str = "",
    ) -> None: ...
    # Same as super.log_error and Logger.error
    def log_error(  # type: ignore[override]
        self,
        msg: str,
        *args: Iterable[str],
        exc_info: _ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
    ) -> None: ...
    # Same as super.write_file but without default values
    def write_file(  # type: ignore[override]
        self, new_text: str, filename: FileDescriptorOrPath, old_text: str, encoding: str | None
    ) -> None: ...
    # filename has to be str
    def print_output(self, old: str, new: str, filename: str, equal: bool) -> None: ...  # type: ignore[override]

def warn(msg: object) -> None: ...
def main(fixer_pkg: str, args: Sequence[AnyStr] | None = None) -> Literal[0, 1, 2]: ...
