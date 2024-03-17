#       / Параметры скрипта /
modules = list()
wallet_mode = 1  # Режим кошельков: 1 - порядок как в файле, 2 - случайный порядок
wallets = open('wallets.txt')  # Файл с приватниками и адресами бирж
gas_price_limit = 1.5  # Лимит цены газа в Эфире

# RPC сетей
linea_rpc = 'https://rpc.linea.build'

txn_delay = [5, 20]  # Перерыв после транзакции
wallet_delay = [15, 100]  # Перерыв между кошельками


#       / Параметры транзы /
gas_price_mult = [1.02, 1.04]  # Наценка на газ
gas_mult = [1.45, 1.75]  # Добавочный процент для количества газа


#       / Параметры операций для квестов /
try_delay = [5, 7]  # Перерыв между доп попытками

# ///// Параметры для квестов Week 1
gamer_boom_enable = 0  # Активны ли модули GamerBoom
gamer_boom_proof_switch = 0  # Включен ли proof GamerBoom

nidum_mint_switch = 0  # Активен ли модуль Nidum минт


# ///// Параметры для квестов Week 2
abyss_world_mint_switch = 0  # Включен ли минт Abyss World

pictographs_enable = 0  # Активны ли модули Pictographs
pictographs_mint_switch = 0  # Включен ли минт nft Pictographs
pictographs_stake_switch = 0  # БОНУСНОЕ | Включен ли стейкинг nft Pictographs

omnisea_mint_switch = 0  # Включен ли минт Omnisea (Satoshi Universe)

yooldo_enable = 1  # Активны ли модули yooldo
daily_switch = 1  # Включен ли модуль Daily Stand-up

# ///// Параметры для квестов Week 3
dmail_switch = 0  # Активен ли модуль Dmail

gamic_switch = 0  # Активен ли модуль Gamic
# Количество эфира, посылаемое на адрес контракта
gamic_eth_value = [0.0000001, 0.0000003]
gamic_eth_digs = 7  # Знаков после запятой для эфира

as_match_mint_switch = 0  # Активен ли модуль AsMatch

bit_avatar_switch = 0  # Активен ли модуль BitAvatar

read_on_switch = 0  # Активен ли модуль ReadOn

sending_me_switch = 0  # Активен ли модуль SendingMe
# Количество эфира, посылаемое на адрес контракта
sending_me_eth_value = [0.00000001, 0.0000003]
sending_me_eth_digs = 8  # Знаков после запятой для эфира


# ///// Параметры для квестов Week 4
sarubol_mint_switch = 0  # Активен ли модуль Sarubol mint
lucky_cat_switch = 0  # Активен ли модуль LuckyCat

#       / Параметры для работы скрипта /
# Запас эфира при переводе на адрес биржи и бридже (ETH), чтобы точно прошло
test_mode = 0
gas_price_ether = 1.5
stop_flag = False
start_flag = False
