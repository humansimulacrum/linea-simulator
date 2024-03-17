import settings
from src.logger import cs_logger
from src.Quests.Week2.yooldo.daily import sending
from src.Quests.Week2.yooldo.trobSwap import swapping
from src.Quests.Week2.Pictographs.mint import minting as pictographs_mint, staking as pictographs_stake
from src.Quests.Week2.AbyssWorld.mint import minting as abyss_mint
from src.Quests.Week2.Omnisea.mint import minting as omnisea_mint
from src.Quests.Week1.GamerBoom.mint import gamer_boom_mint
from src.Quests.Week1.GamerBoom.proof import gamer_boom_proof
from src.Quests.Week3.AsMatch.mint import as_match_mint
from src.Helpers.gasPriceChecker import check_limit
from src.Quests.Week3.Dmail.sendMail import dmail_send
from src.Quests.questHelper import running
from src.Quests.Week3.ReadOn.curate import read_on_curate
from src.Quests.Week3.SendingMe.abuse import sending_me
from src.Quests.Week3.Gamic.swap import gamic_swap
from src.Quests.Week3.BitAvatar.checkIn import bit_avatar
from src.Quests.Week1.TownStory.mint import town_story
from src.Quests.Week4.Sarubol.mint import sarubol_mint
from src.Quests.Week4.Zypher.start import zypher
from src.Quests.Week1.Nidum.mint import nidum_mint
from src.Quests.Week4.LuckyCat.mint import lucky_cat


def quest_ops(wallet, modules):
    for module in modules:

        if module == 'yooldo':
            cs_logger.info(f'    ***   Модуль Yooldo   ***   ')
            if settings.daily_switch == 1:
                check_limit()
                sending(wallet)

            if settings.trob_swap_switch == 1:
                check_limit()
                swapping(wallet)

        if module == 'pictographs':
            cs_logger.info(f'    ***   Модуль Pictographs   ***   ')
            if settings.pictographs_mint_switch == 1:
                check_limit()
                pictographs_mint(wallet)
            if settings.pictographs_stake_switch == 1:
                check_limit()
                pictographs_stake(wallet)

        if module == 'abyss':
            cs_logger.info(f'    ***   Модуль Abyss World   ***   ')
            check_limit()
            abyss_mint(wallet)

        if module == 'omnisea':
            cs_logger.info(f'    ***   Модуль Omnisea  ***   ')
            check_limit()
            omnisea_mint(wallet)

        if module == 'gamerboom':
            cs_logger.info(f'    ***   Модуль GamerBoom  ***   ')
            if settings.gamer_boom_proof_switch == 1:
                check_limit()
                running(wallet, gamer_boom_proof)
            if settings.gamer_boom_mint_switch == 1:
                check_limit()
                running(wallet, gamer_boom_mint)

        if module == 'dmail':
            cs_logger.info(f'    ***   Модуль Dmail  ***   ')
            check_limit()
            running(wallet, dmail_send)

        if module == 'asmatch':
            cs_logger.info(f'    ***   Модуль AsMatch  ***   ')
            check_limit()
            running(wallet, as_match_mint)

        if module == 'readon':
            cs_logger.info(f'    ***   Модуль ReadOn  ***   ')
            check_limit()
            running(wallet, read_on_curate)

        if module == 'sendingme':
            cs_logger.info(f'    ***   Модуль SendingMe  ***   ')
            check_limit()
            running(wallet, sending_me)

        if module == 'gamic':
            cs_logger.info(f'    ***   Модуль Gamic  ***   ')
            check_limit()
            running(wallet, gamic_swap)

        if module == 'bitavatar':
            cs_logger.info(f'    ***   Модуль BitAvatar  ***   ')
            check_limit()
            running(wallet, bit_avatar)

        if module == 'townstory':
            cs_logger.info(f'    ***   Модуль TownStory  ***   ')
            check_limit()
            running(wallet, town_story)

        if module == 'sarubol':
            cs_logger.info(f'    ***   Модуль Sarubol  ***   ')
            check_limit()
            running(wallet, sarubol_mint)

        if module == 'zypher2048':
            cs_logger.info(f'    ***   Модуль Zypher 2048  ***   ')
            check_limit()
            running(wallet, zypher)

        if module == 'nidum':
            cs_logger.info(f'    ***   Модуль Nidum Mint  ***   ')
            check_limit()
            running(wallet, nidum_mint)

        if module == 'luckycat':
            cs_logger.info(f'    ***   Модуль LuckyCat Mint  ***   ')
            check_limit()
            running(wallet, lucky_cat)
