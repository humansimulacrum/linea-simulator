from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.helper import delay_sleep
from src.Helpers.txnHelper import get_txn_dict, exec_txn, check_estimate_gas
import settings
from src.ABIs import Omnisea_ABI


contract_address = linea_net.web3.to_checksum_address('0xecbEE1a087aA83Db1fCC6C2C5eFFC30BCb191589')
contract = linea_net.web3.eth.contract(linea_net.web3.to_checksum_address(contract_address),
                                       abi=Omnisea_ABI)
nft_address = '0x0dE240B2A3634fCD72919eB591A7207bDdef03cd'


def build_txn_mint(wallet):
    try:
        value = contract.functions.fixedFee().call()
        txn_dict = get_txn_dict(wallet.address, linea_net, value)
        txn = contract.functions.mint(
            [wallet.address, nft_address, 1, [], 1, b'']
        ).build_transaction(txn_dict)
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (Omnisea/mint: build_txn) {ex.args}')


def mint_nft(wallet):
    try:
        cs_logger.info(f'Минтим Omnisea Nft')

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
        cs_logger.info(f'Ошибка в (Omnisea/mint: mint_nft) {ex.args}')


def minting(wallet):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        cs_logger.info(f' // Попытка №: {attempt}')
        txn_status = mint_nft(wallet)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])
