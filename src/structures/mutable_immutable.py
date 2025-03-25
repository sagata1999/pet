from collections import (
    namedtuple,
    deque,
    defaultdict,
    OrderedDict,
    Counter,
    ChainMap
)


class ImmutableTypes:
    INTEGER: type[int]
    BOOLEAN: type[bool]
    STRING: type[str]
    TUPLE: type[tuple]
    FROZENSET: type[frozenset]
    NONE_TYPE: type[None]
    NAMED_TUPLE: type[namedtuple]


class MutableTypes:
    LIST: type[list]
    DICT: type[dict]
    SET: type[set]
    BYTEARRAY: type[bytearray]
    DEQUE: type[deque]
    DEFAULT_DICT: type[defaultdict]
    ORDERED_DICT: type[OrderedDict]
    COUNTER: type[Counter]
    CHAIN_MAP: type[ChainMap]


