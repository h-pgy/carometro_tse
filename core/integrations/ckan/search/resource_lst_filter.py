from typing import List, Literal, Callable, overload, Dict
from functools import partial
from ..api import CkanActionApiRequest
from .resource_search import ResourceSearch
from core.utils.inspection import list_open_method_names

class FilterResources:

    def __init__(self, api_obj:CkanActionApiRequest):

        self.api = api_obj
        self.__search_obj = ResourceSearch()

    def __and(self, rsce:dict, filters:List[Callable])->bool:

        for filter in filters:
            if not filter(rsce):
                return False
        return True

    def __or(self, rsce:dict, filters:List[Callable])->bool:

        for filter in filters:
            if filter(rsce):
                return True
        return False

    @overload
    def __filter(self, rsces:List[dict], filters:List[Callable], operator=Literal['and'])->List[dict]:
        ...

    @overload
    def __filter(self, rsces:List[dict], filters:List[Callable], operator=Literal['or'])->List[dict]:
        ...

    def __filter(self, rsces:List[dict], filters:List[Callable], operator=Literal['and','or'])->List[dict]:
        
        if operator == 'and':
            filtered = [rsce for rsce in rsces if self.__and(rsce, filters)]
        
        elif operator == 'or':
            filtered = [rsce for rsce in rsces if self.__or(rsce, filters)]
        else:
            raise NotImplementedError(f'Operator {operator} not implemented.')

        return filtered
    
    def __get_search_func(self, func:str)->Callable:

        try:
            return  getattr(self.__search_obj, func)
        except AttributeError:
            raise NotImplementedError(f'Função de busca {func} não implementada')
        
    @property
    def search_options(self):

        return list_open_method_names(self.__search_obj)

    def __call__(self, pkg_name:str, operator:Literal['and', 'or']='and', 
                 search_options:Dict[str,str]=None, **search_params)->List[dict]:


        rsces =self.api.lst_resources(pkg_name)

        if not search_params:
            return rsces
        
        search_options = search_options or {}
        filters = []
        for func_name, search_term in search_params.items():
            filter_func = self.__get_search_func(func_name)
            filter_func = partial(filter_func, search_term=search_term)
            if func_name in search_options:
                filter_func = partial(filter_func, how=search_options[func_name])
            
            filters.append(filter_func)

        return self.__filter(rsces, filters, operator)


        
