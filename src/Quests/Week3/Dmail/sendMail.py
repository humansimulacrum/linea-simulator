from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from src.ABIs import Dmail_ABI


contract_address = linea_net.web3.to_checksum_address('0xD1A3abf42f9E66BE86cfDEa8c5C2c74f041c5e14')
contract = linea_net.web3.eth.contract(linea_net.web3.to_checksum_address(contract_address),
                                       abi=Dmail_ABI)


class Dmail(Quest):
    title = 'Делаем Dmail транзакцию'

    def build_txn(self, wallet):
        try:
            email = wallet.address + '@dmail.ai'
            em = linea_net.web3.keccak(text=email).hex().removeprefix('0x')
            txn_dict = get_txn_dict(wallet.address, linea_net)
            txn = contract.functions.send_mail(
                em, em
            ).build_transaction(txn_dict)
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (Dmail/sendMail: build_txn) {ex.args}')


dmail_send = Dmail()
