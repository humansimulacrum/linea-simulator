
class Wallet(object):
    def __init__(self, wallet_num, key, address, exchange_address, index):
        self.wallet_num = wallet_num
        self.key = key
        self.address = address
        self.index = index
        self.exchange_address = exchange_address
        self.txn_num = 0
        self.bridge_sum = 0
        self.exc_bal_st = 0
        self.exc_bal_end = 0
        self.fwdx_value = 0
        self.zkdx_value = 0
