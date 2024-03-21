from src.Helpers.helper import sign_msg
from src.networks import linea_net
from json import dumps
import requests


def sign_in_message(wallet):
    message_text = "Please sign this message to confirm you are the owner of this address and Sign in to TrustGo App"
    signature = sign_msg(wallet, message_text, linea_net)
    url = 'https://mp.trustalabs.ai/accounts/check_signed_message'
    data = {
        "mode": "evm", "address": wallet.address,
        "message": message_text,
        "signature": signature,
        "invite_from": {"from": "0", "code": 'EPR0QD9W52I8'}}
    headers = {'Authorization': f'TOKEN null', 'Accept': 'application/json'}
    data_json = dumps(data)
    r = requests.post(url, data=data_json, headers=headers)
    if r.status_code == 200:
        res = [r.json()]
        if res[0]['code'] == 0:
            token_auth = res[0]['data']['token']
            return token_auth
    return -1
