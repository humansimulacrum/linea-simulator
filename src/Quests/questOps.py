import settings
from src.Quests.Week2.yooldo.daily import sending
from src.Quests.Week2.Pictographs.mint import minting as pictographs_mint, staking as pictographs_stake
from src.Quests.Week2.AbyssWorld.mint import minting as abyss_mint
from src.Quests.Week2.Omnisea.mint import minting as omnisea_mint
from src.Quests.Week1.GamerBoom.proof import gamer_boom_proof
from src.Quests.Week3.AsMatch.mint import as_match_mint
from src.Helpers.gasPriceChecker import check_limit
from src.Quests.Week3.Dmail.sendMail import dmail_send
from src.Quests.questHelper import running
from src.Quests.Week3.ReadOn.curate import read_on_curate
from src.Quests.Week3.SendingMe.abuse import sending_me
from src.Quests.Week3.Gamic.swap import gamic_swap
from src.Quests.Week3.BitAvatar.checkIn import bit_avatar
from src.Quests.Week4.Sarubol.mint import sarubol_mint
from src.Quests.Week1.Nidum.mint import nidum_mint
from src.Quests.Week4.LuckyCat.mint import lucky_cat
from src.Quests.Week5.Battlemon.mint import battlemon
from src.Quests.Week5.OmniZone.mint import omni_zone
from src.Quests.Week5.Nouns.mint import nouns_mint


def quest_ops(wallet, modules):
    for module in modules:

        if module == 'yooldo':
            print(f'    ***   Module Yooldo   ***   ')
            if settings.daily_switch == 1:
                check_limit()
                sending(wallet)

        if module == 'pictographs':
            print(f'    ***   Module Pictographs   ***   ')
            if settings.pictographs_mint_switch == 1:
                check_limit()
                pictographs_mint(wallet)
            if settings.pictographs_stake_switch == 1:
                check_limit()
                pictographs_stake(wallet)

        if module == 'abyss':
            print(f'    ***   Module Abyss World   ***   ')
            check_limit()
            abyss_mint(wallet)

        if module == 'omnisea':
            print(f'    ***   Module Omnisea  ***   ')
            check_limit()
            omnisea_mint(wallet)

        if module == 'gamerboom':
            print(f'    ***   Module GamerBoom  ***   ')
            if settings.gamer_boom_proof_switch == 1:
                check_limit()
                running(wallet, gamer_boom_proof)

        if module == 'dmail':
            print(f'    ***   Module Dmail  ***   ')
            check_limit()
            running(wallet, dmail_send)

        if module == 'asmatch':
            print(f'    ***   Module AsMatch  ***   ')
            check_limit()
            running(wallet, as_match_mint)

        if module == 'readon':
            print(f'    ***   Module ReadOn  ***   ')
            check_limit()
            running(wallet, read_on_curate)

        if module == 'sendingme':
            print(f'    ***   Module SendingMe  ***   ')
            check_limit()
            running(wallet, sending_me)

        if module == 'gamic':
            print(f'    ***   Module Gamic  ***   ')
            check_limit()
            running(wallet, gamic_swap)

        if module == 'bitavatar':
            print(f'    ***   Module BitAvatar  ***   ')
            check_limit()
            running(wallet, bit_avatar)

        if module == 'sarubol':
            print(f'    ***   Module Sarubol  ***   ')
            check_limit()
            running(wallet, sarubol_mint)

        if module == 'nidum':
            print(f'    ***   Module Nidum Mint  ***   ')
            check_limit()
            running(wallet, nidum_mint)

        if module == 'luckycat':
            print(f'    ***   Module LuckyCat Mint  ***   ')
            check_limit()
            running(wallet, lucky_cat)

        if module == 'battlemon':
            print(f'    ***   Module Battlemon Mint  ***   ')
            check_limit()
            running(wallet, battlemon)

        if module == 'omnizone':
            print(f'    ***   Module OmniZone Mint  ***   ')
            check_limit()
            running(wallet, omni_zone)

        if module == 'nouns':
            print(f'    ***   Module Nouns Mint  ***   ')
            check_limit()
            running(wallet, nouns_mint)