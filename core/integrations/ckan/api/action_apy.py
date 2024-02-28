from functools import partial

from core.utils import UrlBuildeR, json_get_request
from core.exceptions.ckan import APIResponseError
import urllib3


class CkanActionApiRequest:

    def __init__(self, domain , verify=False):

        build_url = UrlBuildeR(domain)
        self.build_url = partial(build_url, namespace='action')
        #geralmente as APIs do CKAN não tem certificado SSL
        self.verify=verify
        self.disable_ssl_warning()

    def disable_ssl_warning(self):

        if not self.verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __assert_success(self, json_resp):

        if not json_resp.get('success'):
            raise APIResponseError(f'Response Error. Response: {json_resp}')
    
    def __get_endpoint(self, endpoint: str, **params)->list:

        url = self.build_url(endpoint=endpoint, **params)
        print(f'Get request to url: {url}')
        resp = json_get_request(url, verify=self.verify)

        self.__assert_success(resp)

        return resp['result']

    def lst_pkgs(self)->dict:

        pkg_lst_endpoint = 'package_list'

        return self.__get_endpoint(pkg_lst_endpoint)

    def get_package(self, pkg_name: str)->dict:
    
        show_pkg_endpoint = 'package_show'
        
        return self.__get_endpoint(show_pkg_endpoint, id=pkg_name)

    def lst_resources(self, pkg_name: str)->list:

        results = self.get_package(pkg_name)

        return results['resources']