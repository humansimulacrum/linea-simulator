from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Helpers.helper import sign_msg
from src.Quests.questHelper import Quest
from src.ABIs import TownStory_ABI
from src.Quests.Week1.TownStory.sign import get_message, get_txn_signature


contract_address = linea_net.web3.to_checksum_address('0x281A95769916555D1C97036E0331b232b16EdABC')
contract = linea_net.web3.eth.contract(linea_net.web3.to_checksum_address(contract_address),
                                       abi=TownStory_ABI)


class TownStory(Quest):
    title = 'Минтим TownStory'

    def build_txn(self, wallet):
        try:
            message_text = get_message(wallet)
            message_signature = sign_msg(wallet, message_text, linea_net)
            signature, deadline = get_txn_signature(wallet, message_signature)
            txn_dict = get_txn_dict(wallet.address, linea_net)
            txn = contract.functions.createAccountSign(
                signature, 0, deadline
            ).build_transaction(txn_dict)
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (TownStory/mint: build_txn) {ex.args}')


town_story = TownStory()
