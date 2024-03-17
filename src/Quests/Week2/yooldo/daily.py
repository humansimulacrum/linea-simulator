from src.Helpers.txnHelper import exec_txn, check_estimate_gas, get_txn_dict
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.helper import delay_sleep
import settings


def build_txn(wallet):
    try:
        value = linea_net.web3.to_wei(0.000002, 'ether')
        txn = get_txn_dict(wallet.address, linea_net, value)
        txn['to'] = linea_net.web3.to_checksum_address('0x63ce21bd9af8cc603322cb025f26db567de8102b')
        txn['data'] = '0xfb89f3b1'
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (daily: build_txn) {ex.args}')


def daily_check_in(wallet):
    try:
        cs_logger.info(f'Делаем Daily Stand-Up')

        txn = build_txn(wallet)
        estimate_gas = check_estimate_gas(txn, linea_net)
        if type(estimate_gas) is str:
            cs_logger.info(f'{estimate_gas}')
            return False
        else:
            txn['gas'] = estimate_gas
            txn_hash, txn_status = exec_txn(wallet.key, txn, linea_net)
            cs_logger.info(f'Hash: {txn_hash}')

            wallet.txn_num += 1
            delay_sleep(settings.txn_delay[0], settings.txn_delay[1])
            return True

    except Exception as ex:
        cs_logger.info(f'Ошибка в (daily: daily_check_in) {ex.args}')


def sending(wallet):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        cs_logger.info(f' _ Попытка №: {attempt}')
        txn_status = daily_check_in(wallet)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])
