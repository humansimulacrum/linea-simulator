#       / Script params /
modules = list()
wallet_mode = 1  # Wallet mode: 1 - order as in file, 2 - random order
wallets = open('wallets.txt')  # File with private keys
# gas limit linea
gas_price_limit = 0.9
gas_price_net = 0.9


linea_rpc = 'https://rpc.linea.build'

txn_delay = [30, 60]  # Delay between transactions
wallet_delay = [15, 100]  # Delay between wallets

#       / Transaction params /
gas_price_mult = [1.02, 1.04]  # Gas price multiplier
gas_mult = [1.1, 1.2]  # Gas limit multiplier


#       / Quest params /
try_delay = [5, 7]  # Delay between attempts

# ///// Week 1
gamer_boom_enable = 1  # Is GamerBoom module active
gamer_boom_proof_switch = 1  # Is GamerBoom proof enabled

nidum_mint_switch = 1  # Is Nidum Mint Active


# ///// Week 2
abyss_world_mint_switch = 1  # Is Abyss World mint enabled

pictographs_enable = 1  # Is Pictographs module enabled
pictographs_mint_switch = 1  # Is Pictographs mint enabled
pictographs_stake_switch = 0  # Is Pictographs staking enabled

omnisea_mint_switch = 1  # Is Omnisea (Satoshi Universe) mint enabled

yooldo_enable = 1  # Is yooldo enabled
daily_switch = 1  # Is Yooldo Daily Stand-up enabled

# ///// Week 3
dmail_switch = 1  # Is Dmail module enabled
gamic_switch = 1  # Is Gamic module enabled
as_match_mint_switch = 1  # Is AsMatch module enabled
bit_avatar_switch = 1  # Is BitAvatar module enabled
read_on_switch = 1  # Is ReadOn module enabled
sending_me_switch = 1  # Is SendingMe module enabled


# ///// Week 4
sarubol_mint_switch = 1  # Is  Sarubol mint module enabled
lucky_cat_switch = 1  # Is LuckyCat module enabled

# ///// Week 5
omni_zone_switch = 1  # Is OmniZone module enabled
battlemon_switch = 1  # Is Battlemon module enabled


# NOT TESTED
# -----------------
#       / Proof of Humanity params /
poh_enable = 0  # POH Mode | 0 - Disabled, 1 - Enabled, 2 - Only score check

trusta_a_switch = 0  # Is Trusta Group A Enabled
trusta_b_switch = 0  # Is Trusta Group B Enabled
ruby_switch = 0  # Is RubyScore Group B Enabled


# Replace attestation with another one (better score)?
trusta_a_replace_enable = 0
trusta_b_replace_enable = 0
ruby_replace_enable = 0


# Advanced

# Gamic swap range
gamic_eth_value = [0.0000001, 0.000003]
gamic_eth_digs = 7  # precision

# Sending me sending range
sending_me_eth_value = [0.00000001, 0.000003]
sending_me_eth_digs = 8  # precision


test_mode = 0
last_row = 1
last_row_poh = 1
stop_flag = False
start_flag = False
