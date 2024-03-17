from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class LuckyCat(Quest):
    title = 'Минтим LuckyCat'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address('0xc577018b3518cD7763D143d7699B280d6E50fdb6')
            txn['data'] = '0x70245bdc'
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (LuckyCat/mint: build_txn) {ex.args}')


lucky_cat = LuckyCat()
