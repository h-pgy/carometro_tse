from datetime import datetime
from core.exceptions.misc import DatetimeOutOfFormat

def str_to_full_date_hour(date_string:str)->datetime:

    try:
        datetime_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')

        return datetime_obj
    except ValueError as e:
        raise DatetimeOutOfFormat(str(e))

