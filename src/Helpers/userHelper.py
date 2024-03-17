import settings
import settings as stgs
from src.networks import linea_net


def get_info(wallets):
    print(
        f'Цена газа в Linea: {linea_net.web3.from_wei(linea_net.web3.eth.gas_price, "gWei")} gWei')

    print(
        f'Задержки между кошельками: от {stgs.wallet_delay[0]} до {stgs.wallet_delay[1]} сек')
    print(
        f'Задержки между транзакциями: от {stgs.txn_delay[0]} до {stgs.txn_delay[1]} сек')

    if stgs.gamer_boom_enable == 1:
        if stgs.gamer_boom_proof_switch == 1:
            print('Модуль GamerBoom Proof Включен')
        else:
            print('Модуль GamerBoom Proof Отключен')

    else:
        print('Квесты GamerBoom Отключены')

    if stgs.nidum_mint_switch == 1:
        print('Модуль Nidum Nft Включен')
    else:
        print('Модуль Nidum Nft Отключен')

    if stgs.yooldo_enable == 1:
        if stgs.daily_switch == 1:
            print('Модуль Daily Stand-Up Включен')
        else:
            print('Модуль Daily Stand-Up Отключен')

    else:
        print('Квесты Yooldo Отключены')

    if stgs.pictographs_enable == 1:
        if stgs.pictographs_mint_switch == 1:
            print('Модуль Pictographs Mint Включен')
        else:
            print('Модуль Pictographs Mint Отключен')

        if stgs.pictographs_stake_switch == 1:
            print('Модуль Pictographs Stake Включен')
        else:
            print('Модуль Pictographs Stake Отключен')
    else:
        print('Квесты Pictographs Отключены')

    if stgs.abyss_world_mint_switch == 1:
        print('Модуль Abyss World Включен')
    else:
        print('Модуль Abyss World Отключен')

    if stgs.omnisea_mint_switch == 1:
        print('Модуль Omnisea Включен')
    else:
        print('Модуль Omnisea Отключен')

    if stgs.dmail_switch == 1:
        print('Модуль Dmail Включен')
    else:
        print('Модуль Dmail Отключен')

    if stgs.as_match_mint_switch == 1:
        print('Модуль AsMatch Включен')
    else:
        print('Модуль AsMatch Отключен')

    if stgs.read_on_switch == 1:
        print('Модуль ReadOn Включен')
    else:
        print('Модуль ReadOn Отключен')

    if stgs.sending_me_switch == 1:
        print('Модуль SendingMe Включен')
    else:
        print('Модуль SendingMe Отключен')

    if stgs.gamic_switch == 1:
        print('Модуль Gamic Включен')
    else:
        print('Модуль Gamic Отключен')

    if stgs.bit_avatar_switch == 1:
        print('Модуль BitAvatar Включен')
    else:
        print('Модуль BitAvatar Отключен')

    if stgs.sarubol_mint_switch == 1:
        print('Модуль Sarubol Включен')
    else:
        print('Модуль Sarubol Отключен')

    if stgs.lucky_cat_switch == 1:
        print('Модуль LuckyCat Включен')
    else:
        print('Модуль LuckyCat Отключен')

    while True:
        print(f'Подтвердить? Y/N: ')
        answer = input('')
        if answer.lower() == 'y':
            stgs.start_flag = True
            break
        if answer.lower() == 'n':
            break
