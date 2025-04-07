from collections import ChainMap, Counter, OrderedDict, defaultdict, deque
from typing import Any, NamedTuple


class ImmutableTypes:
    INTEGER: type[int] = int
    BOOLEAN: type[bool] = bool
    STRING: type[str] = str
    TUPLE: type[tuple[Any, ...]] = tuple
    FROZENSET: type[frozenset[Any]] = frozenset
    NONE_TYPE: None = None
    NAMED_TUPLE: type[NamedTuple] = NamedTuple


class MutableTypes:
    LIST: type[list[Any]] = list
    DICT: type[dict[Any, Any]] = dict
    SET: type[set[Any]] = set
    BYTEARRAY: type[bytearray] = bytearray
    DEQUE: type[deque[Any]] = deque
    DEFAULT_DICT: type[defaultdict[Any, Any]] = defaultdict
    ORDERED_DICT: type[OrderedDict[Any, Any]] = OrderedDict
    COUNTER: type[Counter[Any]] = Counter
    CHAIN_MAP: type[ChainMap[Any, Any]] = ChainMap


class UpperStr(str):
    def __new__(cls, value):
        print("Calling __new__")
        return super().__new__(cls, value.upper())

    def __init__(self, value):
        print("Calling __init__")
