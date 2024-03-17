from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class GamerBoomProof(Quest):
    title = 'Делаем Proof GamerBoom'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address('0x6CD20be8914A9Be48f2a35E56354490B80522856')
            txn['data'] = '0xb9a2092d'
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (GamerBoom/proof: build_txn) {ex.args}')


gamer_boom_proof = GamerBoomProof()
