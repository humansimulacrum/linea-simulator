from web3 import Web3
import settings
import time

web3 = Web3(Web3.HTTPProvider(settings.ethereum_rpc))


def check_gas_price_ether():
    gas_price_now = web3.eth.gas_price
    settings.gas_price_ether = web3.from_wei(gas_price_now, 'gWei')


def checking():
    while settings.stop_flag is False:
        check_gas_price_ether()
        time.sleep(15 * 1)


def check_limit():
    if settings.gas_price_ether > settings.gas_price_limit:
        while settings.gas_price_ether > settings.gas_price_limit:
            wait_anim('|', settings.gas_price_ether)
            time.sleep(0.4)
            wait_anim('/', settings.gas_price_ether)
            time.sleep(0.4)
            wait_anim('--', settings.gas_price_ether)
            time.sleep(0.4)
            wait_anim('\ ', settings.gas_price_ether)
            time.sleep(0.4)


def wait_anim(symbol, gas_price):
    print(f'\rЖдем, цена газа большая: {int(gas_price)} gWei  {symbol} ', end='')
