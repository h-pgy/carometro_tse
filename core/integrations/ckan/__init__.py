from .api.action_apy import CkanActionApiRequest
from config import CKAN_DOMAIN

ckan = CkanActionApiRequest(CKAN_DOMAIN)