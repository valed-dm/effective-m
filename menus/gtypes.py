"""Generic types used in functions annotations"""

from typing import Callable, Dict, Tuple, Union

from pandas import DataFrame

row_type = Tuple[str, str, str, str, str, str,]
data_type = Union[
    str,
    Tuple[str],
    Dict[str, str],
    Dict[str, Tuple[str, str]],
    row_type
]
handler_type = Union[
    Callable[[row_type], None],
    Callable[[str, str], None],
    Callable[[Dict[str, str], str], DataFrame],
    Callable[[dict[str, tuple[str]], str], DataFrame],
    Callable[[Dict[str, Tuple[str, str]], str], None]
]
