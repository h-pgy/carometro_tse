
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
