from core.utils import search_string, str_to_full_date_hour
from core.utils.decorators import missing_key_to_false, datetime_out_format_to_false, boolean_return
from typing import List, Literal, Callable, Union, overload
from datetime import datetime
from ..api import CkanActionApiRequest


class ResourceSearch:

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

# criar uma classe para abstrair isso igual fiz com search string    
"""     @missing_key_to_false
    @datetime_out_format_to_false
    def created_before(self, rsce:dict, date:datetime)->bool:

        created_at = self.__extract_datetime(rsce, 'created')

        return created_at <= date

    @missing_key_to_false
    @datetime_out_format_to_false
    def created_after(self, rsce:dict, date:datetime)->bool:

        created_at = self.__extract_datetime(rsce, 'created')

        return created_at >= date
    
    @missing_key_to_false
    @datetime_out_format_to_false
    def modified_before(self, rsce:dict, date:datetime)->bool:

        modified_at = self.__extract_datetime(rsce, 'last_modified')

        return modified_at <= date

    @missing_key_to_false
    @datetime_out_format_to_false
    def modified_after(self, rsce:dict, date:datetime)->bool:

        modified_at = self.__extract_datetime(rsce, 'last_modified')

        return modified_at >= date """
    

    
    