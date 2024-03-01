from core.utils import search_string
from typing import List, Literal
from ..api import CkanActionApiRequest


class PkgSearch:

    def __init__(self, api_obj:CkanActionApiRequest)->None:

        self.api = api_obj

        #keep them in cache
        self.pkgs = self.api.lst_pkgs()

    def search(self, term:str, how:Literal['regex', 'substring', 'literal'], 
               case_insensitive:bool=True, pkg_list:List[str]=None)->List[str]:

        pkg_list = pkg_list or self.pkgs
        return [search_string(term, pkg_list, case_insensitive, how)]
    
    def __call__(self, term:str, how:Literal['regex', 'substring', 'literal']='substring', 
               case_insensitive:bool=True, pkg_list:List[str]=None)->List[str]:
        
        return self.search(term, how, case_insensitive, pkg_list)

    
