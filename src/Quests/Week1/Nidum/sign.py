from src.Helpers.helper import sign_msg
from json import dumps
import random

import requests


def load_proxy():
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return random.choice(proxies) if proxies else None

def register_wallet(wallet, proxies):
    url = f'https://auth.sidusheroes.com/api/v1/users'
    headers = {'Content-Type': 'application/json'}
    data = {'address': wallet.address.lower()}
    json_data = dumps(data)
    requests.post(url, data=json_data, headers=headers, proxies=proxies)


def get_msg(wallet, proxies):
    url = 'https://auth.sidusheroes.com/api/v1/users/' + wallet.address.lower()
    r = requests.get(url, proxies=proxies)
    response = r.json()
    nonce = response['data']['nonce']
    msg_text = f'Please sign this message to connect to sidusheroes.com: {nonce}'
    return msg_text


def auth(wallet, signature, proxies):
    data = {"address": f"{wallet.address}", "signature": f"{signature}"}
    json_data = dumps(data)
    url = 'https://auth.sidusheroes.com/api/v1/auth'
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json_data, headers=headers, proxies=proxies)
    response = r.json()
    bearer = response['data']['accessToken']
    return bearer


def get_token_data(wallet, bearer, proxies):
    url = f'https://plsrv.sidusheroes.com/shadow-game-linea/api/v1/item'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearer}'}
    data = {"user": f"{wallet.address.lower()}", "contract": "0x34Be5b8C30eE4fDe069DC878989686aBE9884470", "tokenId": 9}
    json_data = dumps(data)
    r = requests.post(url, data=json_data, headers=headers, proxies=proxies)


def get_claim_data(wallet, bearer, proxies):
    url = 'https://plsrv.sidusheroes.com/shadow-game-linea/api/v1/claim'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearer}',
               'Content-Length': '151', 'If-None-Match': 'W/"81-IPXBWNB48bs1CNK6NL+XgeHJooA"'}
    data = {"contract": "0x34Be5b8C30eE4fDe069DC878989686aBE9884470",
            "user": f'{wallet.address.lower()}',
            "tokensData": [{"tokenId": 9, "amount": 1}]}
    json_data = dumps(data)
    r = requests.post(url, data=json_data, headers=headers, proxies=proxies)
    response = r.json()
    return response


def request_ops(wallet, net):
    proxy = load_proxy()  # Load the proxy
    if proxy:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
    else:
        proxies = None  # Fallback in case no proxy is available

    register_wallet(wallet, proxies)
    msg_text = get_msg(wallet, proxies)
    signature = sign_msg(wallet, msg_text, net)  # Assuming sign_msg doesn't need proxy modification
    bearer = auth(wallet, signature, proxies)
    get_token_data(wallet, bearer, proxies)
    claim_data = get_claim_data(wallet, bearer, proxies)
    return claim_data