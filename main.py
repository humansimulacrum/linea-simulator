import src.Helpers.helper as helper
import settings
import random
import src.Helpers.gasPriceChecker as gPC
import src.Helpers.userHelper as userHelper
from threading import Thread
from src.Quests.questHelper import get_modules_list
from src.Quests.questOps import quest_ops


wallets = helper.read_wallets()


def main():
    op = 0
    if settings.wallet_mode == 2:
        random.shuffle(wallets)
    for wallet in wallets:
        op += 1

        modules = get_modules_list()
        quest_ops(wallet, modules)

        # Транзакции POH
        proof_op(wallet)

        gPC.check_limit()


# '''
print(f'Wallets found: {len(wallets)}')
userHelper.get_info(wallets)
if settings.start_flag is True:
    gPC.check_gas_price_ether()
    check_thread = Thread(target=gPC.checking, args=(), daemon=True)
    main_thread = Thread(target=main, args=())
    check_thread.start()
    main_thread.start()
    main_thread.join()
    print(f'Press Enter to exit')
    input()
    print(f'Exiting...')
# '''
