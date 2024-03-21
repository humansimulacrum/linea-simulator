from src.networks import linea_net
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class BitAvatar(Quest):
    title = 'Doing Check In in BitAvatar'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address(
                '0x37D4BFc8c583d297A0740D734B271eAc9a88aDe4')
            txn['data'] = '0x183ff085'
            return txn
        except Exception as ex:
            print(f'Error in (BitAvatar/checkIn: build_txn) {ex.args}')


bit_avatar = BitAvatar()
