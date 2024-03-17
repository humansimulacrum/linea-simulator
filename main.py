import src.Helpers.helper as helper
import src.networks as nt
import settings
import random
import src.logger as logger
import src.Helpers.gasPriceChecker as gPC
import src.Helpers.userHelper as userHelper
from threading import Thread
from src.Quests.questHelper import get_modules_list
from src.Quests.questOps import quest_ops
from src.POH.proofOps import proof_op


logger.create_xml()
settings.last_row = logger.get_last_row_overall()
wallets = helper.read_wallets()
net_src = nt.arbitrum_net


def main():
    op = 0
    if settings.wallet_mode == 2:
        random.shuffle(wallets)
    for wallet in wallets:
        op += 1
        balance_st = nt.linea_net.web3.from_wei(
            nt.linea_net.web3.eth.get_balance(wallet.address), 'ether')
        logger.cs_logger.info(f'')
        logger.cs_logger.info(
            f'№ {op} ({wallet.wallet_num})  Адрес: {wallet.address}  Биржа: {wallet.exchange_address}')
        script_time = helper.get_curr_time()

        balance_end = nt.linea_net.web3.from_wei(
            nt.linea_net.web3.eth.get_balance(wallet.address), 'ether')
        nonce = nt.linea_net.web3.eth.get_transaction_count(wallet.address)
        logger.write_overall(wallet, balance_st,
                             balance_end, script_time, nonce)

        modules = get_modules_list()
        quest_ops(wallet, modules)

        gPC.check_limit()

        # Транзакции POH
        proof_op(wallet)

        balance_end = nt.linea_net.web3.from_wei(
            nt.linea_net.web3.eth.get_balance(wallet.address), 'ether')
        nonce = nt.linea_net.web3.eth.get_transaction_count(wallet.address)
        logger.write_overall(wallet, balance_st,
                             balance_end, script_time, nonce)

        # Депозит на биржу или бридж


# '''
logger.cs_logger.info(f'Найдено кошельков: {len(wallets)}')
userHelper.get_info(wallets)
if settings.start_flag is True:
    gPC.check_gas_price_ether()
    check_thread = Thread(target=gPC.checking, args=(), daemon=True)
    main_thread = Thread(target=main, args=())
    check_thread.start()
    main_thread.start()
    main_thread.join()
    logger.cs_logger.info(f'Нажмите Enter для выхода')
    input()
    logger.cs_logger.info(f'Выход...')
# '''
