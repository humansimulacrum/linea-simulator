from random import shuffle
from src.networks import linea_net
import settings
from src.Helpers.txnHelper import check_estimate_gas, exec_txn
from src.Helpers.helper import delay_sleep


class Quest(object):
    title = 'Выполняем квестик'

    def build_txn(self, wallet):
        pass


def get_modules_list():
    modules = list()
    # Операции
    if settings.yooldo_enable == 1:
        modules.append('yooldo')
        shuffle(modules)

    if settings.pictographs_enable == 1:
        modules.append('pictographs')
        shuffle(modules)

    if settings.abyss_world_mint_switch == 1:
        modules.append('abyss')
        shuffle(modules)

    if settings.omnisea_mint_switch == 1:
        modules.append('omnisea')
        shuffle(modules)

    if settings.gamer_boom_enable == 1:
        modules.append('gamerboom')
        shuffle(modules)

    if settings.dmail_switch == 1:
        modules.append('dmail')
        shuffle(modules)

    if settings.as_match_mint_switch == 1:
        modules.append('asmatch')
        shuffle(modules)

    if settings.read_on_switch == 1:
        modules.append('readon')
        shuffle(modules)

    if settings.sending_me_switch == 1:
        modules.append('sendingme')
        shuffle(modules)

    if settings.gamic_switch == 1:
        modules.append('gamic')
        shuffle(modules)

    if settings.bit_avatar_switch == 1:
        modules.append('bitavatar')
        shuffle(modules)

    if settings.sarubol_mint_switch == 1:
        modules.append('sarubol')
        shuffle(modules)

    if settings.nidum_mint_switch == 1:
        modules.append('nidum')
        shuffle(modules)

    if settings.lucky_cat_switch == 1:
        modules.append('luckycat')
        shuffle(modules)

    if settings.battlemon_switch == 1:
        modules.append('battlemon')
        shuffle(modules)

    if settings.omni_zone_switch == 1:
        modules.append('omnizone')
        shuffle(modules)

    if settings.nouns_swich == 1:
        modules.append('nouns')
        shuffle(modules)

    return modules


def run_quest(wallet, quest):
    try:
        print(f'{quest.title}')
        txn = quest.build_txn(wallet)
        estimate_gas = check_estimate_gas(txn, linea_net)
        if type(estimate_gas) is str:
            print(f'{estimate_gas}')
            return False
        else:
            txn['gas'] = estimate_gas
            txn_hash, txn_status = exec_txn(wallet.key, txn, linea_net)
            print(f'Hash: {txn_hash}')

            wallet.txn_num += 1
            delay_sleep(settings.txn_delay[0], settings.txn_delay[1])
            return True

    except Exception as ex:
        print(f'Error in (questHelper: run_quest) {ex.args}')


def running(wallet, quest):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        print(f' // Attempt №: {attempt}')
        txn_status = run_quest(wallet, quest)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])
