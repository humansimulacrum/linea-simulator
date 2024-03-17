from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest
from src.Quests.Week1.Nidum.sign import request_ops
from src.ABIs import Nidum_ABI


contract_address = linea_net.web3.to_checksum_address('0x34Be5b8C30eE4fDe069DC878989686aBE9884470')
contract = linea_net.web3.eth.contract(linea_net.web3.to_checksum_address(contract_address),
                                       abi=Nidum_ABI)


class Nidum(Quest):
    title = 'Минтим Nidum'

    def build_txn(self, wallet):
        try:
            claim_data = request_ops(wallet, linea_net)
            message = claim_data['message']
            signature = claim_data['signature']
            txn_dict = get_txn_dict(wallet.address, linea_net)
            txn = contract.functions.mintFromShadowBatch(
                [9], [1], 0, message, signature
            ).build_transaction(txn_dict)
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (Nidum/mint: build_txn) {ex.args}')


nidum_mint = Nidum()
