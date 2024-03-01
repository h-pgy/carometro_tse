from core.exceptions.misc import DatetimeOutOfFormat

def missing_key_to_false(func):
    '''Overrides a function that may throw an 
    KeyError and makes it return false instead'''

    def wrapper(*args, **kwargs):

        try:
            result= func(*args, **kwargs)
            return result
        except KeyError as e:
            print(f'Missing key: {e}')
            return False
    
    return wrapper

def datetime_out_format_to_false(func):
    '''Overrides a function that may throw an 
    DatetimeOutOfFormat and makes it return false instead'''

    def wrapper(*args, **kwargs):

        try:
            result= func(*args, **kwargs)
            return result
        except DatetimeOutOfFormat as e:
            print(f'Datetime out of format: {e}')
            return False
    
    return wrapper

def boolean_return(func):
    '''Overrides a function that may return any object and converts if to boolean'''

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return bool(result)
    
    return wrapper