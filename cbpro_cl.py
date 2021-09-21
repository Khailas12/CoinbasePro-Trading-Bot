import cbpro
from config import CB_CREDENTIALS


def get_client(credentials):
    'Returns the cbpto AuthenticatedClent using credentials from parameters dict'
    
    cbpro_client = cbpro.AuthenticatedClient(
        credentials['KEY'],
        credentials['SECRET'],
        credentials['PASSPHRASE'],
        api_urk=credentials['URL']
        )

def cbpro_client(func):
    def function_wrapper(*args, **kwargs):
        cbpro_client = get_client(CB_CREDENTIALS)
        resp = func(cbpro_client = cbpro_client, *args, *kwargs)
        
        return resp
    return function_wrapper
