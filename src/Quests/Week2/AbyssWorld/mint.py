import eth_abi
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.helper import delay_sleep
from src.Helpers.txnHelper import get_txn_dict, exec_txn, check_estimate_gas
import settings


def build_txn(wallet):
    try:
        value = linea_net.web3.to_wei(0.0001, 'ether')
        txn = get_txn_dict(wallet.address, linea_net, value)
        txn['to'] = linea_net.web3.to_checksum_address('0x66Ccc220543B6832f93c2082EDD7be19c21dF6C0')
        txn['data'] = '0xefef39a1' + eth_abi.encode(['uint256'], [1]).hex()
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (daily: build_txn) {ex.args}')


def mint_nft(wallet):
    try:
        cs_logger.info(f'Минтим Abyss World Nft')

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
        cs_logger.info(f'Ошибка в (Pictographs/mint: stake_nft) {ex.args}')


def minting(wallet):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        cs_logger.info(f' // Попытка №: {attempt}')
        txn_status = mint_nft(wallet)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])
