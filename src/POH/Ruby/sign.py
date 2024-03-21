from src.Helpers.helper import sign_msg
from src.networks import linea_net
import requests


def sign_in_message(wallet):
    message_text = " A signature is required for authorization on the platform and does not pose a threat to users!"
    signature = sign_msg(wallet, message_text, linea_net)
    url = (f'https://rubyscore.io/api/auth/login?signature='
           f'{signature}'
           f'&message=+A+signature+is+required+for+authorization+on+the+platform+and+does+not+pose+a+threat+to+users!'
           f'&wallet={wallet.address}')
    headers = {'Accept': 'application/json'}
    r = requests.post(url, headers=headers)
    if r.status_code == 200:
        res = [r.json()]
        token_auth = res[0]['result']['token']
        return token_auth
    return -1
