import eth_abi
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class Sarubol(Quest):
    title = 'Минтим Tanukiverse для Sarubol'

    def build_txn(self, wallet):
        try:
            mint_value = linea_net.web3.to_wei(0.0001, 'ether')
            txn = get_txn_dict(wallet.address, linea_net, mint_value)
            txn['to'] = linea_net.web3.to_checksum_address('0x47874ff0BEf601D180a8A653A912EBbE03739a1a')
            txn['data'] = '0xefef39a1' + eth_abi.encode(['uint256'], [1]).hex()
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (Sarubol/mint: build_txn) {ex.args}')


sarubol_mint = Sarubol()
