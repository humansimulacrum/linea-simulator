from src.Helpers.txnHelper import exec_txn, check_estimate_gas, get_txn_dict, approve_amount
from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.helper import delay_sleep, get_random_value
import settings
import eth_abi
from src.Swaps.tokens import USDC_token, contract_USDC, TROB_token
from src.Swaps.iZUMiSwapUSDC import swap_eth_to_usdc
from src.Swaps.swapHelper import get_eth_value


swap_contract_address = linea_net.web3.to_checksum_address('0x6c5f2ce8ab5d6341ba9563c82ca7fa6fa0c35161')


def build_txn_swap(wallet, usdc_value):
    try:
        txn = get_txn_dict(wallet.address, linea_net)
        txn['to'] = swap_contract_address
        txn['data'] = '0x0c0a7630' + eth_abi.encode(['address', 'address', 'uint256'],
                                                    [USDC_token.address, TROB_token.address, usdc_value]).hex()
        txn['gas'] = 200000
        return txn
    except Exception as ex:
        cs_logger.info(f'Ошибка в (trobSwap: build_txn_swap) {ex.args}')


def swap_usdc_to_trob(wallet):
    try:
        usdc_balance = contract_USDC.functions.balanceOf(wallet.address).call()
        if usdc_balance < int(0.01*10**6):
            eth_value = get_eth_value(settings.usdc_limits)
            swap_eth_to_usdc(wallet, eth_value)
            usdc_swap_balance = contract_USDC.functions.balanceOf(wallet.address).call()
        else:
            usdc_swap_balance = int(get_random_value(settings.usdc_limits[0], settings.usdc_limits[1], 2) * 10 ** 6)
            if usdc_balance < usdc_swap_balance:
                usdc_swap_balance = usdc_balance
        usdc_value = (usdc_swap_balance // 10 ** 4) * 10 ** 4
        if usdc_value <= 9999:
            return False
        cs_logger.info(f'Делаем свап {(usdc_value / 10 ** 6)} USDC на TROB')
        approve_amount(wallet.key, wallet.address, swap_contract_address, contract_USDC, linea_net,
                       usdc_value, usdc_value)
        txn = build_txn_swap(wallet, usdc_value)
        estimate_gas = check_estimate_gas(txn, linea_net)
        if type(estimate_gas) is str:
            cs_logger.info(f'{estimate_gas}')
            return False
        else:
            txn['gas'] = estimate_gas
            txn_hash, txn_status = exec_txn(wallet.key, txn, linea_net)
            cs_logger.info(f'Hash: {txn_hash}')

            wallet.txn_num += 1
            delay_sleep(settings.txn_delay[0], settings.txn_delay[1])
            return True

    except Exception as ex:
        cs_logger.info(f'Ошибка в (trobSwap: swap_usdc_to_trob) {ex.args}')


def swapping(wallet):
    attempt = 1
    txn_status = False
    while txn_status is False and attempt < 4:
        cs_logger.info(f' _ Попытка №: {attempt}')
        txn_status = swap_usdc_to_trob(wallet)
        attempt += 1
        if txn_status is False:
            delay_sleep(settings.try_delay[0], settings.try_delay[1])
