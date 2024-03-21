import settings
import settings as stgs
from src.networks import linea_net


def get_info(wallets):
    print(
        f'Linea gas price : {linea_net.web3.from_wei(linea_net.web3.eth.gas_price, "gWei")} gWei')

    print(
        f'Delay between wallets: from {stgs.wallet_delay[0]} to {stgs.wallet_delay[1]} s')
    print(
        f'Delay between transactions: from {stgs.txn_delay[0]} to {stgs.txn_delay[1]} s')

    if stgs.gamer_boom_enable == 1:
        if stgs.gamer_boom_proof_switch == 1:
            print('Module GamerBoom Proof Enabled')
        else:
            print('Module GamerBoom Proof Disabled')

    else:
        print('Quests GamerBoom Disabled')

    if stgs.nidum_mint_switch == 1:
        print('Module Nidum Nft Enabled')
    else:
        print('Module Nidum Nft Disabled')

    if stgs.yooldo_enable == 1:
        if stgs.daily_switch == 1:
            print('Module Daily Stand-Up Enabled')
        else:
            print('Module Daily Stand-Up Disabled')

    else:
        print('Quests Yooldo Disabled')

    if stgs.pictographs_enable == 1:
        if stgs.pictographs_mint_switch == 1:
            print('Module Pictographs Mint Enabled')
        else:
            print('Module Pictographs Mint Disabled')

        if stgs.pictographs_stake_switch == 1:
            print('Module Pictographs Stake Enabled')
        else:
            print('Module Pictographs Stake Disabled')
    else:
        print('Quests Pictographs Disabled')

    if stgs.abyss_world_mint_switch == 1:
        print('Module Abyss World Enabled')
    else:
        print('Module Abyss World Disabled')

    if stgs.omnisea_mint_switch == 1:
        print('Module Omnisea Enabled')
    else:
        print('Module Omnisea Disabled')

    if stgs.dmail_switch == 1:
        print('Module Dmail Enabled')
    else:
        print('Module Dmail Disabled')

    if stgs.as_match_mint_switch == 1:
        print('Module AsMatch Enabled')
    else:
        print('Module AsMatch Disabled')

    if stgs.read_on_switch == 1:
        print('Module ReadOn Enabled')
    else:
        print('Module ReadOn Disabled')

    if stgs.sending_me_switch == 1:
        print('Module SendingMe Enabled')
    else:
        print('Module SendingMe Disabled')

    if stgs.gamic_switch == 1:
        print('Module Gamic Enabled')
    else:
        print('Module Gamic Disabled')

    if stgs.bit_avatar_switch == 1:
        print('Module BitAvatar Enabled')
    else:
        print('Module BitAvatar Disabled')

    if stgs.sarubol_mint_switch == 1:
        print('Module Sarubol Enabled')
    else:
        print('Module Sarubol Disabled')

    if stgs.lucky_cat_switch == 1:
        print('Module LuckyCat Enabled')
    else:
        print('Module LuckyCat Disabled')

    while True:
        print(f'Confirm? Y/N: ')
        answer = input('')
        if answer.lower() == 'y':
            stgs.start_flag = True
            break
        if answer.lower() == 'n':
            break
