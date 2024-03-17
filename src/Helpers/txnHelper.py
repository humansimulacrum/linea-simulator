import settings
import time
import src.logger as logger
import src.Helpers.helper as helper
import src.ABIs as ABIs


Gas_oracle_address = '0x420000000000000000000000000000000000000F'


def get_txn_dict(address, network, value=0):
    gas_price = get_gas_price(network)
    nonce = network.web3.eth.get_transaction_count(address)
    dict_transaction = {
        'chainId': network.chain_id,
        'from': address,
        'value': value,
        'gas': 650000,
        'gasPrice': gas_price,
        'nonce': nonce,
    }
    return dict_transaction


def get_gas_price(network):
    gas_price_mult = helper.get_random_value(
        settings.gas_price_mult[0], settings.gas_price_mult[1], 3)
    gas_price = int(network.web3.eth.gas_price * gas_price_mult)
    return gas_price


def check_tx_status(txn_hash, net, sec=3):
    status = None
    while status is None:
        txn_done = net.web3.eth.wait_for_transaction_receipt(txn_hash, 60 * 5)
        status = txn_done.get('status')
        time.sleep(sec)
    return status


def approve_amount(private_key, address, spender_address, token_contract, net, token_amount, approve_sum=2 ** 256 - 1):
    try:
        allowance = token_contract.functions.allowance(
            address, spender_address).call()
        decimals = token_contract.functions.decimals().call()
        logger.cs_logger.info(
            f'Сумма токена разрешенная смартконтракту: {allowance / 10 ** decimals}')
        if allowance < token_amount:
            logger.cs_logger.info(
                f'Даем разрешение смартконтракту использовать токен')

            nonce = net.web3.eth.get_transaction_count(address)
            gas_price = net.web3.eth.gas_price

            dict_transaction_approve = {
                'from': address,
                'chainId': net.chain_id,
                'gas': 650000,
                'gasPrice': gas_price,
                'nonce': nonce,
            }
            txn_approve = token_contract.functions.approve(
                spender_address,
                approve_sum
            ).build_transaction(dict_transaction_approve)

            estimate_gas = check_estimate_gas(txn_approve, net)
            txn_approve['gas'] = estimate_gas

            txn_hash, txn_status = exec_txn(private_key, txn_approve, net,)
            return txn_hash
    except Exception as ex:
        logger.cs_logger.info(
            f'Ошибка в (txnHelper: approve_amount): {ex.args}')


def check_estimate_gas(txn, net):
    try:
        gas_mult = helper.get_random_value(
            settings.gas_mult[0], settings.gas_mult[1], 3)
        estimate_gas = int(net.web3.eth.estimate_gas(txn) * gas_mult)
        return estimate_gas
    except Exception as ex:
        return f'Ошибка в (txnHelper: check_estimate_gas): {ex.args}'


def exec_txn(private_key, txn, net):
    try:
        if settings.test_mode == 0:
            signed_txn = net.web3.eth.account.sign_transaction(
                txn, private_key)
            txn_hash = net.web3.eth.send_raw_transaction(
                signed_txn.rawTransaction)
            check_tx_status(txn_hash, net, 3)
            return txn_hash.hex(), True
        if settings.test_mode == 1:
            txn_hash = 'Test'  # Для тестов
            return txn_hash, True
    except Exception as ex:
        return f'Ошибка в (exec_txn): {ex.args}', False
