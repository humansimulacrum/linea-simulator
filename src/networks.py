import settings
from web3 import Web3


class Network(object):
    def __init__(self, name, rpc, chain_id_l0, transfer, bridge_gas, router_eth_address, router_address, chain_okx):
        self.name = name
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.chain_id = self.web3.eth.chain_id
        self.chain_id_l0 = chain_id_l0
        self.transfer = transfer
        self.bridge_gas = bridge_gas
        self.router_eth_address = router_eth_address
        self.router_address = router_address
        self.chain_okx = chain_okx


networks = list()

linea_net = Network(
    name='Linea',
    rpc=settings.linea_rpc,
    chain_id_l0=183,
    transfer=[80_000, 150_000],
    bridge_gas=[700_000, 900_000],
    router_eth_address='0x8731d54E9D02c286767d56ac03e8037C07e01e98',
    router_address='0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590',
    chain_okx='ETH-Linea'
)

ethereum_net = Network(
    name='Ethereum',
    rpc=settings.ethereum_rpc,
    chain_id_l0=101,
    transfer=[80_000, 150_000],
    bridge_gas=[580_000, 650_000],
    router_eth_address='0x150f94B44927F078737562f0fcF3C95c01Cc2376',
    router_address='0x8731d54E9D02c286767d56ac03e8037C07e01e98',
    chain_okx='ETH-ERC20'
)

arbitrum_net = Network(
    name='Arbitrum',
    rpc=settings.arbitrum_rpc,
    chain_id_l0=110,
    transfer=[600_000, 1_500_000],
    bridge_gas=[4_000_000, 5_000_000],
    router_eth_address='0xbf22f0f184bCcbeA268dF387a49fF5238dD23E40',
    router_address='0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614',
    chain_okx='ETH-Arbitrum One'
)

optimism_net = Network(
        name='Optimism',
        rpc=settings.optimism_rpc,
        chain_id_l0=111,
        transfer=[80_000, 150_000],
        bridge_gas=[700_000, 900_000],
        router_eth_address='0xB49c4e680174E331CB0A7fF3Ab58afC9738d5F8b',
        router_address='0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
        chain_okx='ETH-Optimism'
    )

networks.extend([arbitrum_net, optimism_net])  # Сети для Stargate бриджа
