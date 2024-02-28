
import requests
from ..exceptions.ckan import APIRequestError

def json_get_request(url, verify=False):

    #muitas apis do CKAN não tem SSL configurado   
    with requests.get(url, verify=verify) as r:
        if not r.status_code==200:
            raise APIRequestError(f'Request Error. Status code: {r.status_code}: {r.reason}')
        return r.json()