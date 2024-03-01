from .url_builder import UrlBuildeR
from .string_search import StringSearch
from .requests import json_get_request
from .unzip import unzip_from_bytes
from .datetime import str_to_full_date_hour, datetime_to_day_precision, DateTimeSearch
from .decorators import boolean_return

search_string = StringSearch()
datetime_search = DateTimeSearch()
boolean_search_string = boolean_return(search_string)
boolean_datetime_search = boolean_return(datetime_search)