from datetime import datetime
from typing import Union, List, Callable, Literal, overload
from core.exceptions.misc import DatetimeOutOfFormat

def str_to_full_date_hour(date_string:str)->datetime:

    try:
        datetime_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')

        return datetime_obj
    except ValueError as e:
        raise DatetimeOutOfFormat(str(e))

def datetime_to_day_precision(dt_hour:datetime)->datetime:

    components = []
    params = ('year', 'month', 'day')
    for param in params:
        try:
            extracted = getattr(dt_hour, param)
            components.append(extracted)
        except AttributeError as e:
            raise DatetimeOutOfFormat(str(e))

    return datetime(**dict(zip(params, components)))

class DateTimeSearch:


    def __solve_haystack_type(self, haystack:Union[datetime, List[datetime]])->List[datetime]:

        if type(haystack) is datetime:
            return [haystack]
        return haystack
        
    def __base_search(self, needle:datetime, haystack:Union[datetime, List[datetime]], 
                      callback:Callable, day_precision=bool)->List[datetime]:

        haystack = self.__solve_haystack_type(haystack)
        matches = []

        for hay in haystack:
            if day_precision:
                hay = datetime_to_day_precision(hay)
                needle = datetime_to_day_precision(needle)

            if callback(needle, hay):
                matches.append(hay)
        
        return matches

    @overload
    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], callback:Callable, day_precision:bool,
                search_type:Literal['after'])->List[datetime]:
        ...

    @overload
    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], callback:Callable, day_precision:bool,
               search_type:Literal['after_equals'])->List[datetime]:
        ...
    
    @overload
    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], callback:Callable, day_precision:bool,
               search_type:Literal['before'])->List[datetime]:
        ...
    
    @overload
    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], callback:Callable, day_precision:bool,
               search_type:Literal['before_equals'])->List[datetime]:
        ...

    @overload
    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], callback:Callable, day_precision:bool,
               search_type:Literal['equals'])->List[datetime]:
        ...

    def search(self, needle:datetime, haystack:Union[datetime, List[datetime]], day_precision:bool, 
                search_type:Literal['after', 'after_equals', 'before', 'before_equals', 'equals'])->List[datetime]:
        
        if search_type=='after':

            filtered = self.__base_search(needle, haystack, 
                                          lambda needle, haystack:needle<haystack,
                                          day_precision=day_precision)

        elif search_type=='after_equals':

            filtered = self.__base_search(needle, haystack, 
                                          lambda needle, haystack:needle<=haystack,
                                          day_precision=day_precision)
        elif search_type=='before':

            filtered = self.__base_search(needle, haystack, 
                                          lambda needle, haystack:needle>haystack,
                                          day_precision=day_precision)
        elif search_type=='before_equals':

            filtered = self.__base_search(needle, haystack, 
                                          lambda needle, haystack:needle>=haystack,
                                          day_precision=day_precision)
        elif search_type=='equals':

            filtered = self.__base_search(needle, haystack, 
                                          lambda needle, haystack:needle==haystack,
                                          day_precision=day_precision)
                
        else:
            raise NotImplementedError(f'Search type {search_type} not implemented.')
        
        return filtered 

    def __call__(self, needle:datetime, haystack:Union[datetime, List[datetime]], day_precision:bool, 
                search_type:Literal['after', 'after_equals', 'before', 'before_equals', 'equals'])->List[datetime]:
        
        return self.search(needle, haystack, day_precision, search_type)