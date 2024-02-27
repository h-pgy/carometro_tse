import os
from typing import Union
from dotenv import load_dotenv

def copy_dot_env_example():

    if not os.path.exists('.env'):
        print('Definindo o ambiente a partir da cópia do arquivo .env.example.')
        with open('.env.example', 'r') as example:
            with open('.env', 'w') as env_file:
                env_file.write(example.read())



def load_env():

    copy_dot_env_example()
    load_dotenv()

def load_env_var(varname:str)->Union[int, float, str]:

    try:
        return os.environ[varname]
    except KeyError:
        raise RuntimeError(f'Variavel de ambiente {varname} não definida.')
    

CKAN_DOMAIN=load_env_var('TSE_CKAN_DOMAIN') 