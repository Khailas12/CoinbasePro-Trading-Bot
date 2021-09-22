from cbpro_cl import cbpro_client
from logger import logger


@cbpro_client
def get_deposit_account(cbpro_client):  
    """ GET ID of account's ACH bank acconnt (assumes there's only one)
    
    Params:
        - None
    Return
        - account: dict
        {
            {
                "allow_buy": bool,
                "allow_deposit": bool,
                "allow_sell": bool,
                "allow_withdraw: bool,
                "cdv_status": str,
                "created_at": time, 
                "currency": str,
                "id": str,
                "limits": dict,
                "name": str,
                "primary_buy": bool,
                "primary_sell": bool,
                "resource": str,
                "resource_path": str,
                "type": str,
                "updated_at": time,
                "verification": str,
                "verified": bool
            }
        }
    """
    
    bank_accounts = cbpro_client.get_payment_methods()
    
    for account in bank_accounts:
        if account['type'] == 'ach_bank_account':
            return account
        
        
@logger   
@cbpro_client
def deposit_funds(cbpro_client, deposit_amount = 10):   # default deposit amount is $10
    """ Makes deposit into USD Wallet
    Params:
        - deposit_amount: int (default 10)
    Return: 
        - deposit response
        {
            "id": str,
            "amount": str,
            "currency": "USD",
            "payout_at": str(datetime)
        }
    """
    
    logger.info('Gettng account ID')
    deposit_account_id = get_deposit_account()['id']
    logger.info('Account ID: {}'.format(deposit_account_id))
    
    resp = cbpro_client.deposit(deposit_amount, 'USD', deposit_account_id)
    
    if 'message' in resp.keys():
        logger.warning('In sandbox mode, unable to make deposit')
    else:
        logger.info('Deposit response: {}'.format(resp))
    
    return resp