from core.utils import search_string, str_to_full_date_hour, datetime_search
from core.utils.decorators import missing_key_to_false, datetime_out_format_to_false, boolean_return
from typing import Literal
from datetime import datetime


class ResourceSearch:

    def __init__(self, day_precision=True)->None:

        self.day_precision=day_precision

    def __extract_datetime(self, rsce:dict, key:str)->datetime:

        return str_to_full_date_hour(rsce[key])

    def __extract_string(self, rsce:dict, key:str, lower=True)->str:

        val = rsce[key]
        return str(val).lower()
    
    @missing_key_to_false
    @boolean_return
    def format(self, rsce:dict, search_term:str, how:Literal['regex', 'substring', 'literal']='literal')->bool:

        val = self.__extract_string(rsce, 'format')
        return search_string(search_term, val, True, search_type=how)

    @missing_key_to_false
    @boolean_return
    def mimetype(self, rsce:dict, search_term:str, how:Literal['regex', 'substring', 'literal']='literal')->bool:

        val = self.__extract_string(rsce, 'mimetype')
        return search_string(search_term, val, True, search_type=how)
    
    @missing_key_to_false
    @boolean_return
    def name(self, rsce:dict, search_term:str, how:Literal['regex', 'substring', 'literal']='substring')->bool:

        val = self.__extract_string(rsce, 'name')
        return search_string(search_term, val, True, search_type=how)
    
    @missing_key_to_false
    @boolean_return
    def description(self, rsce:dict, search_term:str, how:Literal['regex', 'substring', 'literal']='substring')->bool:

        val = self.__extract_string(rsce, 'description')
        return search_string(search_term, val, True, search_type=how)
    
    @missing_key_to_false
    @boolean_return
    def id(self, rsce:dict, search_term:str, how:Literal['regex', 'substring', 'literal']='literal')->bool:

        val = self.__extract_string(rsce, 'id')
        return search_string(search_term, val, True, search_type=how)
    
    @missing_key_to_false
    @datetime_out_format_to_false
    def created(self, rsce:dict, search_term:datetime, 
                how:Literal['after', 'after_equals', 'before', 'before_equals', 'equals']='equals')->bool:

        val = self.__extract_datetime(rsce, 'created')
        return datetime_search(search_term, val, self.day_precision, how)
    
    @missing_key_to_false
    @datetime_out_format_to_false
    def last_modified(self, rsce:dict, search_term:datetime, 
                how:Literal['after', 'after_equals', 'before', 'before_equals', 'equals']='equals')->bool:

        val = self.__extract_datetime(rsce, 'last_modified')
        return datetime_search(search_term, val, self.day_precision, how)
    

    
    