import random
import src.logger as logger
import time
import math
from web3 import Web3
import settings
from src.Wallet import Wallet
import datetime
import requests
from eth_account.messages import encode_defunct


def sign_msg(wallet, message_text, net):
    text_hex = "0x" + message_text.encode('utf-8').hex()
    text_encoded = encode_defunct(hexstr=text_hex)
    signed_message = net.web3.eth.account.sign_message(text_encoded, private_key=wallet.key)
    signature = signed_message.signature
    return signature.hex()


def get_curr_time():
    script_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
    return script_time


def get_price(token_name):
    url = f'https://min-api.cryptocompare.com/data/price?fsym={token_name}&tsyms=USDT&api_key=c8a5e2ad37b494efbbd89af2f4edb232353d228e93406615a36b273c0fccd4f2'
    response = requests.get(url)
    try:
        result = [response.json()]
        price = result[0]['USDT']
    except Exception as error:
        logger.cs_logger.info(f'{error.args}')
        price = 2370
    return price


def read_wallets():
    wallet_list = list()
    wallet_info = settings.wallets.read().splitlines()
    index = 1
    w3 = Web3()
    for wl in wallet_info:
        num = wl.split(', ')[0]
        wallet_num = int(num)
        key = wl.split(', ')[1]
        address = w3.eth.account.from_key(key).address
        exchange = wl.split(', ')[2]
        exc_address = Web3.to_checksum_address(exchange)
        wlt = Wallet(wallet_num, key, address, exc_address, index)
        index += 1
        wallet_list.append(wlt)
    return wallet_list


def check_balance_change(wallet, balance, net_dst, timeout, period=20):
    end_time = time.time() + timeout
    while time.time() < end_time:
        new_balance = net_dst.web3.eth.get_balance(wallet.address)
        if balance == new_balance:
            time.sleep(period)
        else:
            return new_balance
    return balance


def delay_sleep(min_delay, max_delay):
    delay = random.randint(min_delay, max_delay)
    logger.cs_logger.info(f'Делаем перерыв в {delay} сек')
    time.sleep(delay)
    return delay


def get_random_value(min_value, max_value, digs=5):
    random_value = random.uniform(min_value, max_value)
    trunc = math.trunc(random_value * (10 ** digs))  # Округляем до {digs} знаков после запятой
    random_value_tr = trunc / (10 ** digs)
    return random_value_tr


def trunc_value(value, digs_min, digs_max):
    digs = random.randint(digs_min, digs_max)
    trunc = math.trunc(value * (10 ** digs))  # Округляем до {digs} знаков после запятой
    value_tr = trunc / (10 ** digs)
    return value_tr


def choice_net(networks, net_name):
    for net in networks:
        if net.name == net_name:
            return net
