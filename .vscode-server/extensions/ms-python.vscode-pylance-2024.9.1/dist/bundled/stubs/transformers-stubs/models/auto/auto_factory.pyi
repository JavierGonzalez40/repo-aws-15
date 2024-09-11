import os
from collections import OrderedDict
from collections.abc import Iterator
from typing import Any
from typing_extensions import TypeAlias

from transformers.configuration_utils import PretrainedConfig
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast

from .configuration_auto import AutoConfig as AutoConfig

_LazyAutoMappingValue: TypeAlias = tuple[
    # Tokenizers will depend on packages installed, too much variance and there are no common base or Protocol
    type[Any | None],
    type[PreTrainedTokenizerFast | None],
]

CLASS_DOCSTRING: str
FROM_CONFIG_DOCSTRING: str
FROM_PRETRAINED_TORCH_DOCSTRING: str
FROM_PRETRAINED_TF_DOCSTRING: str
FROM_PRETRAINED_FLAX_DOCSTRING: str

class _BaseAutoModelClass:
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def from_config(cls, config, **kwargs): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: str | os.PathLike[str], *model_args, **kwargs): ...
    @classmethod
    def register(cls, config_class, model_class) -> None: ...

def insert_head_doc(docstring, head_doc: str = ""): ...
def auto_class_update(cls, checkpoint_for_example: str = "bert-base-cased", head_doc: str = ""): ...
def get_values(model_mapping): ...
def getattribute_from_module(module, attr): ...

class _LazyAutoMapping(OrderedDict[type[PretrainedConfig], _LazyAutoMappingValue]):
    def __init__(self, config_mapping, model_mapping) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: type[PretrainedConfig]) -> _LazyAutoMappingValue: ...
    def keys(self) -> list[type[PretrainedConfig]]: ...
    def get(self, key: type[PretrainedConfig], default: _LazyAutoMappingValue) -> _LazyAutoMappingValue: ...
    def __bool__(self) -> bool: ...
    def values(self) -> list[_LazyAutoMappingValue]: ...
    def items(self) -> list[tuple[type[PretrainedConfig], _LazyAutoMappingValue]]: ...
    def __iter__(self) -> Iterator[type[PretrainedConfig]]: ...
    def __contains__(self, item: object) -> bool: ...
    def register(self, key: type[PretrainedConfig], value: _LazyAutoMappingValue) -> None: ...
