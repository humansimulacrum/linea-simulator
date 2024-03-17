from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.helper import delay_sleep
from src.Helpers.txnHelper import get_txn_dict, exec_txn, check_estimate_gas
import settings
from src.ABIs import Pictographs_ABI


contract_address = linea_net.web3.to_checksum_address('0xb18b7847072117AE863f71F9473D555d601Eb537')
contract = linea_net.web3.eth.contract(linea_net.web3.to_checksum_address(contract_address),
                                       abi=Pictographs_ABI)


def build_txn_mint(wallet):
    try:
        value = contract.functions.price().call()
        txn = get_txn_dict(wallet.address, linea_net, value)
        txn['to'] = contract_address
        txn['data'] = '0x14f710fe'
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (Pictographs/mint: build_txn) {ex.args}')


def build_txn_stake(wallet):
    try:
        nft_id = contract.functions.tokenOfOwnerByIndex(wallet.address, 0).call()
        txn_dict = get_txn_dict(wallet.address, linea_net)
        txn = contract.functions.stake(
            nft_id
        ).build_transaction(txn_dict)
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (Pictographs/mint: build_txn_stake) {ex.args}')


def mint_nft(wallet):
    try:
        cs_logger.info(f'Минтим Pictographs Nft')

        txn = build_txn_mint(wallet)
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
        cs_logger.info(f'Ошибка в (Pictographs/mint: mint_nft) {ex.args}')


def stake_nft(wallet):
    try:
        cs_logger.info(f'Стейкаем Pictographs Nft')

        txn = build_txn_stake(wallet)
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


def staking(wallet):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        cs_logger.info(f' // Попытка №: {attempt}')
        txn_status = stake_nft(wallet)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])