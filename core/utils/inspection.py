import inspect
from typing import Any, List

def list_method_names(obj:Any)->List[str]:

    methods = inspect.getmembers(obj, predicate=inspect.ismethod)
    return [m[0] for m in methods]

def list_open_method_names(obj:Any)->List[str]:

    methods = inspect.getmembers(obj, predicate=inspect.ismethod)
    return [m[0] for m in methods if not m[0].startswith('_')]