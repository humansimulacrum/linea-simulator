import eth_abi
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from random import randint


class ReadOn(Quest):
    title = 'Делаем транзакцию ReadOn'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address('0x8286d601a0ed6cf75E067E0614f73A5b9F024151')
            content_url = randint(1709924291302671616, 18446744073709551614)
            txn['data'] = '0x7859bb8d' + eth_abi.encode(['uint64'], [content_url]).hex()
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (ReadOn/curate: build_txn) {ex.args}')


read_on_curate = ReadOn()
