from src.Helpers.helper import sign_msg
from json import dumps
import requests


def register_wallet(wallet):
    url = f'https://auth.sidusheroes.com/api/v1/users'
    headers = {'Content-Type': 'application/json'}
    data = {'address': wallet.address.lower()}
    json_data = dumps(data)
    requests.post(url, data=json_data, headers=headers)


def get_msg(wallet):
    url = 'https://auth.sidusheroes.com/api/v1/users/' + wallet.address.lower()
    r = requests.get(url)
    response = r.json()
    nonce = response['data']['nonce']
    msg_text = f'Please sign this message to connect to sidusheroes.com: {nonce}'
    return msg_text


def auth(wallet, signature):
    data = {"address": f"{wallet.address}", "signature": f"{signature}"}
    json_data = dumps(data)
    url = 'https://auth.sidusheroes.com/api/v1/auth'
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json_data, headers=headers)
    response = r.json()
    bearer = response['data']['accessToken']
    return bearer


def get_token_data(wallet, bearer):
    url = f'https://plsrv.sidusheroes.com/shadow-game-linea/api/v1/item'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearer}'}
    data = {"user": f"{wallet.address.lower()}", "contract": "0x34Be5b8C30eE4fDe069DC878989686aBE9884470", "tokenId": 9}
    json_data = dumps(data)
    r = requests.post(url, data=json_data, headers=headers)


def get_claim_data(wallet, bearer):
    url = 'https://plsrv.sidusheroes.com/shadow-game-linea/api/v1/claim'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearer}',
               'Content-Length': '151', 'If-None-Match': 'W/"81-IPXBWNB48bs1CNK6NL+XgeHJooA"'}
    data = {"contract": "0x34Be5b8C30eE4fDe069DC878989686aBE9884470",
            "user": f'{wallet.address.lower()}',
            "tokensData": [{"tokenId": 9, "amount": 1}]}
    json_data = dumps(data)
    r = requests.post(url, data=json_data, headers=headers)
    response = r.json()
    return response


def request_ops(wallet, net):
    register_wallet(wallet)
    msg_text = get_msg(wallet)
    signature = sign_msg(wallet, msg_text, net)
    bearer = auth(wallet, signature)
    get_token_data(wallet, bearer)
    claim_data = get_claim_data(wallet, bearer)
    return claim_data

