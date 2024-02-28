import re
from re import Pattern
from typing import Union, Callable, List, Literal, overload


class StringSearch:

    def __re_pattern_search(self, patt:Union[str, Pattern], resource:str)->bool:
        '''Finds resource based on a RegeX pattern search'''

        if re.match(patt, resource):
            return True
        return False
    
    def __substring_search(self, substring:str, resource:str)->bool:
        '''Finds resource based on substring containment.'''

        return substring in resource
    
    def __literal_search(self, string:str, resource:str)->bool:
        '''Finds resource based on literal equality to a string'''

        return string == resource
    
    def __case_insentive(self, resource:str)->str:

        return resource.lower().strip()
    
    def __base_search(self, needle:str, haystack:List[str], case_insensitve:bool, callback:Callable)->List[str]:

        matches = []

        for resource in haystack:
            if case_insensitve:
                resource = self.__case_insentive(resource)
            if callback(needle, resource):
                matches.append(resource)
        
        return matches
    
    @overload
    def search(self, needle:str, haystack:List[str], case_insensitve:bool, 
               earch_type:Literal['regex'])->List[str]:

        ...

    @overload
    def search(self, needle:str, haystack:List[str], case_insensitve:bool, 
               search_type:Literal['substring'])->List[str]:
        
        ...
    
    @overload
    def search(self, needle:str, haystack:List[str], case_insensitve:bool, 
               search_type:Literal['literal'])->List[str]:
        
        ...
    

    def search(self, needle:str, haystack:List[str], case_insensitve:bool, 
                search_type:str)->List[str]:
        
        if search_type=='regex':

            needle = re.compile(needle)
            filtered = self.__base_search(needle, haystack, case_insensitve, 
                                  self.__re_pattern_search)

        elif search_type=='substring':

            filtered = self.__base_search(needle, haystack, case_insensitve, 
                                  self.__re_pattern_search)
            
        elif search_type=='literal':
            filtered = self.__base_search(needle, haystack, case_insensitve, 
                                  self.__re_pattern_search)
        else:
            raise NotImplementedError(f'Search type {search_type} not implemented.')
        
        return filtered

    def __call__(self,needle:str, haystack:List[str], case_insensitve:bool, 
                search_type:str)->List[str]:
        
        return self.search(needle, haystack, case_insensitve, search_type)