from time import time
from json import dumps
import requests


def get_time_nonce():
    time_nonce = int(time() / 86400)
    return time_nonce


def get_address_line(address):
    address_line = (address[:19] + '...' + address[-18:]).lower()
    return address_line


def get_message(wallet):
    nonce = get_time_nonce()
    address_line = get_address_line(wallet.address)
    message = ('Welcome to Town Story! \n\n'
               'Click to sign in and accept the Town Story\n'
               'Terms of Service:\n'
               'https://townstory.io/\n\n'
               'This request will not trigger a blockchain\n'
               'transaction or cost any gas fees.\n\n'
               'Your authentication status will reset after\n'
               'each session.\n\n'
               'Wallet address:\n'
               f'{address_line}\n\n'
               f'Nonce: {nonce}')
    return message


def get_txn_signature(wallet, message_signature):
    data = {"header": {"version": "1.0.1", "baseVersion": "1.0.0", "referer": ""},
            "transaction": {"func": "register.loginByWallet",
                            "params": {"hall": 0, "wallet": "metamask", "chain": "linea",
                                       "signature": message_signature, "address": wallet.address}}}
    json_data = dumps(data)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url1 = 'https://aws-login.townstory.io/town-login/handler.php'
    r = requests.get(url1, data=json_data, headers=headers)
    response = r.json()
    if response['result'] != 'failed':
        txn_signature = r.json()['response']['signature']
        deadline = r.json()['response']['deadline']
        return txn_signature, deadline
