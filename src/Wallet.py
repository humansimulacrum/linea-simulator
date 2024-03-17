
class Wallet(object):
    def __init__(self, key, address, index):
        self.key = key
        self.address = address
        self.index = index
        self.txn_num = 0
