from _typeshed import Incomplete

EPSILON: float

def linear(middle, pos): ...
def curved(middle, pos): ...
def sine(middle, pos): ...
def sphere_increasing(middle, pos): ...
def sphere_decreasing(middle, pos): ...

SEGMENTS: Incomplete

class GradientFile:
    gradient: Incomplete
    def getpalette(self, entries: int = 256): ...

class GimpGradientFile(GradientFile):
    gradient: Incomplete
    def __init__(self, fp) -> None: ...
