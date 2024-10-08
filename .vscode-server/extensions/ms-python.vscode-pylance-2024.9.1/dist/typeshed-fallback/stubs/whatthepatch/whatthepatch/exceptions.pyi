class WhatThePatchException(Exception): ...

class HunkException(WhatThePatchException):
    hunk: int | None
    def __init__(self, msg: str, hunk: int | None = None) -> None: ...

class ApplyException(WhatThePatchException): ...

class SubprocessException(ApplyException):
    code: int
    def __init__(self, msg: str, code: int) -> None: ...

class HunkApplyException(HunkException, ApplyException, ValueError): ...
class ParseException(HunkException, ValueError): ...
