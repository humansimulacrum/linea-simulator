from src.networks import linea_net
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class Battlemon(Quest):
    title = 'Minting Battlemon'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address(
                '0x578705C60609C9f02d8B7c1d83825E2F031e35AA')
            txn['data'] = '0x6871ee40'
            return txn
        except Exception as ex:
            print(f'Error in (Battlemon/mint: build_txn) {ex.args}')


battlemon = Battlemon()
