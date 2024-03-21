from src.networks import linea_net
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class GamerBoomMint(Quest):
    title = 'Minting GamerBoom'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address(
                '0xc0B4ab5CB0Fdd6f5DFddb2F7C10c4c6013F97bF2')
            txn['data'] = '0x1249c58b'
            return txn
        except Exception as ex:
            print(f'Error in (GamerBoom/mint: build_txn) {ex.args}')


gamer_boom_mint = GamerBoomMint()
