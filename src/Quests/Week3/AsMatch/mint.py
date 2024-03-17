import eth_abi
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class AsMatchMint(Quest):
    title = 'Минтим AsMatch'

    def build_txn(self, wallet):
        try:
            value = linea_net.web3.to_wei(0.0001, 'ether')
            txn = get_txn_dict(wallet.address, linea_net, value)
            txn['to'] = linea_net.web3.to_checksum_address('0xc043bce9aF87004398181A8de46b26e63B29bf99')
            txn['data'] = '0xefef39a1' + eth_abi.encode(['uint256'], [1]).hex()
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (AsMatch/mint: build_txn) {ex.args}')


as_match_mint = AsMatchMint()
