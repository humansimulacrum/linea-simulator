from src.POH.Trusta.attestA import attest_a, score_check as trust_a_check
from src.POH.Trusta.attestB import attest_b, score_check as trust_b_check
from src.POH.Ruby.attest import attest_ruby, score_check as ruby_check
import settings
from random import shuffle
from src.Helpers.gasPriceChecker import check_limit


def proof_op(wallet):
    if settings.poh_enable == 1:
        proof_list = list()

        if settings.trusta_a_switch == 1:
            proof_list.append('trustaA')
            shuffle(proof_list)

        if settings.trusta_b_switch == 1:
            proof_list.append('trustaB')
            shuffle(proof_list)

        if settings.ruby_switch == 1:
            proof_list.append('ruby')
            shuffle(proof_list)

        for attest in proof_list:
            if attest == 'trustaA':
                check_limit()
                attest_a(wallet)

            if attest == 'trustaB':
                check_limit()
                attest_b(wallet)

            if attest == 'ruby':
                check_limit()
                attest_ruby(wallet)

    if settings.poh_enable == 2:
        trust_a_check(wallet)
        trust_b_check(wallet)
        ruby_check(wallet)
