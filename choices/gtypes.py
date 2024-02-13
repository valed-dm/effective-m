from typing import Callable, Dict, List, Tuple, Union

from pandas import DataFrame

data_type = Union[
    None,
    str,
    Tuple[str],
    Dict[str, str],
    Dict[str, tuple[str, str]],
]

handler_type = Union[
    Callable[[List[str], str], None],  # create
    Callable[[Dict[str, Tuple[str, str]], str], None],  # update
    Callable[[str, str], None],  # delete
    Callable[[Dict[str, str], str], DataFrame],  # row_result
    Callable[[Dict[str, Tuple[str]], str], DataFrame],  # column_result
]
