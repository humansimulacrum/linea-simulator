from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from src.Helpers.helper import get_random_value
import settings


class Gamic(Quest):
    title = 'Делаем свап в Gamic'

    def build_txn(self, wallet):
        try:
            value_wei = linea_net.web3.to_wei(get_random_value(settings.gamic_eth_value[0],
                                                               settings.gamic_eth_value[1],
                                                               settings.gamic_eth_digs), 'ether')
            txn = get_txn_dict(wallet.address, linea_net, value_wei)
            txn['to'] = linea_net.web3.to_checksum_address('0xe5d7c2a44ffddf6b295a15c148167daaaf5cf34f')
            txn['data'] = '0xd0e30db0'
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (Gamic/swap: build_txn) {ex.args}')


gamic_swap = Gamic()
