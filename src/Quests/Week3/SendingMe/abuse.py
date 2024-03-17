import settings
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from src.Helpers.helper import get_random_value


class SendingMe(Quest):
    title = 'Делаем SendingMe транзакцию'

    def build_txn(self, wallet):
        try:
            value_wei = linea_net.web3.to_wei(get_random_value(settings.sending_me_eth_value[0],
                                                               settings.sending_me_eth_value[1],
                                                               settings.sending_me_eth_digs), 'ether')
            txn = get_txn_dict(wallet.address, linea_net, value_wei)
            txn['to'] = linea_net.web3.to_checksum_address('0xc0DEb0445e1c307b168478f38eac7646d198F984')
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (SendingMe/abuse: build_txn) {ex.args}')


sending_me = SendingMe()
