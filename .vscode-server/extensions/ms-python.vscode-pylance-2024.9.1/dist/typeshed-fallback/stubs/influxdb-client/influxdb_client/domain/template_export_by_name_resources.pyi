from _typeshed import Incomplete

class TemplateExportByNameResources:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, kind: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
