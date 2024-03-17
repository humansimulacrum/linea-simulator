import settings
from web3 import Web3


class Network(object):
    def __init__(self, name, rpc):
        self.name = name
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.chain_id = self.web3.eth.chain_id


networks = list()

linea_net = Network(
    name='Linea',
    rpc=settings.linea_rpc,
)
