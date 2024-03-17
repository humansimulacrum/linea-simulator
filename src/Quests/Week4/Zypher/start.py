import eth_abi
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from random import choice


class Zypher(Quest):
    title = 'Делаем транзу для Zypher 2048'

    def build_txn(self, wallet):
        try:
            symbols = '0123456789abcdef'
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address('0x490d76b1e9418a78b5403740bd70dfd4f6007e0f')
            data_line = ''.join([choice(symbols) for _ in range(64)])
            txn['data'] = '0x36ab86c4' + data_line + eth_abi.encode(['uint256'], [1]).hex()
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (Zypher/start: build_txn) {ex.args}')


zypher = Zypher()
