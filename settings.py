

#       / Параметры скрипта /
modules = list()
wallet_mode = 1  # Режим кошельков: 1 - порядок как в файле, 2 - случайный порядок
wallets = open('wallets.txt')  # Файл с приватниками и адресами бирж
log_file = 'LineaPark logs.xlsx'  # Файл логов
gas_price_limit = 40  # Лимит цены газа в Эфире


#       / Параметры биржи /
api_key = ''  # Ключ API основного аккаунта биржи
secret_key = ''  # Секретный ключ
pass_phrase = ''  # Пасс-фраза

exc_withdraw = 0  # Вывод с биржи на кошельки: 0 - выкл / 1 - вкл
exc_deposit = 0  # Депозит с кошельков на биржу: 0 - выкл / 1 - вкл

exc_mode = 3  # Режим вывода средств с биржи: 1 - часть от баланса | 2 - весь доступный баланс | 3 - число в ед. эфира
exc_percent = [0.3, 0.4]  # Процент баланса, который будем выводить с биржи

exc_sum = [0.04, 0.06]  # Количество эфира, которое выводим с биржи
exc_sum_digs = [3, 5]  # количество знаков для округления суммы вывода с биржи

# Верхняя граница суммы вывода с биржи при выводе процента от баланса (в единицах эфира)
exc_limit_max = 2
exc_percent_step = 0.05  # Шаг, с которым уменьшаются границы процента баланса

# Остаток на кошельке при переводе на адрес биржи (ETH)
deposit_remains = [0.0048, 0.0085]
deposit_digs = 5  # Количество знаков после запятой для остатка на кошельке

# Минимальное количество знаков после запятой для суммы вывода с биржи (при % от баланса)
exc_digs_min = 4
# Максимальное количество знаков после запятой для суммы вывода с биржи (при % от баланса)
exc_digs_max = 5


#       / RPC сетей /
ethereum_rpc = 'https://1rpc.io/eth'
linea_rpc = 'https://rpc.linea.build'
arbitrum_rpc = 'https://1rpc.io/arb'
optimism_rpc = 'https://1rpc.io/op'


#       / Параметры модулей /
# 0 - Вывод сразу из Linea на биржу | 1 - Бридж в Arbitrum, затем вывод на биржу
switch_bridge_exc = 0


#       / Параметры перерывов /
bridge_delay = [10, 15]  # Перерыв после поступления средств в сеть назначения
txn_delay = [5, 20]  # Перерыв после транзакции
wallet_delay = [15, 100]  # Перерыв между кошельками


#       / Параметры бриджа /
bridge_sum_mode = 1  # 1 - Бридж всего эфира, 2 - Бридж процента от баланса
bridge_sum_percent = [0.015, 0.021]  # Процент, который бриджим
bridge_sum_percent_digs = 3  # Количество знаков для процента
# Количество знаков после запятой для округления суммы бриджа
bridge_sum_digs = [4, 6]
# Минимальный и максимальный множитель цены газа для транзакции бриджа
random_mult = [1.15, 1.20]

#   Старгейт бридж
net_bridge = ['Arbitrum', 'Optimism']
slippage = 0.010  # Проскальзывание для бриджа (например: 0.005 = 0.5 %)


#       / Параметры транзы /
gas_price_mult = [1.02, 1.04]  # Наценка на газ
gas_mult = [1.45, 1.75]  # Добавочный процент для количества газа


#       / Параметры Proof of Humanity  /
poh_enable = 0  # Включены ли транзакции POH
trusta_a_switch = 1  # Включен ли модуль Trusta Group A
trusta_b_switch = 1  # Включен ли модуль Trusta Group B
ruby_switch = 1  # Включен ли модуль RubyScore Group B


#       / Параметры операций для квестов /
try_delay = [5, 7]  # Перерыв между доп попытками

# ///// Параметры для квестов Week 1
gamer_boom_enable = 0  # Активны ли модули GamerBoom
# Включен ли минт GamerBoom - НЕ НУЖЕН, засчитываает без него.
gamer_boom_mint_switch = 0
gamer_boom_proof_switch = 1  # Включен ли proof GamerBoom

nidum_mint_switch = 0  # Активен ли модуль Nidum минт

town_story_switch = 0  # Активен ли модуль TownStory


# ///// Параметры для квестов Week 2
abyss_world_mint_switch = 0  # Включен ли минт Abyss World

pictographs_enable = 0  # Активны ли модули Pictographs
pictographs_mint_switch = 1  # Включен ли минт nft Pictographs
pictographs_stake_switch = 1  # БОНУСНОЕ | Включен ли стейкинг nft Pictographs

omnisea_mint_switch = 0  # Включен ли минт Omnisea (Satoshi Universe)

yooldo_enable = 0  # Активны ли модули yooldo
daily_switch = 1  # Включен ли модуль Daily Stand-up
trob_swap_switch = 1  # БОНУСНОЕ | Включен ли модуль свапа USDC на TROB
# Количество USDC, которое свапаем на TROB. Если USDC нет на балансе, то сначала ETH на USDC на указанные значения.
usdc_limits = [0.01, 0.3]
# Количество знаков после запятой для числа эфира, которое свапаем на USDC
eth_volume_digs = [5, 6]
slippage_USDC = 0.020  # slippage для свапов эфира на USDC и обратно


# ///// Параметры для квестов Week 3
dmail_switch = 0  # Активен ли модуль Dmail

gamic_switch = 0  # Активен ли модуль Gamic
# Количество эфира, посылаемое на адрес контракта
gamic_eth_value = [0.0000001, 0.000003]
gamic_eth_digs = 7  # Знаков после запятой для эфира

as_match_mint_switch = 0  # Активен ли модуль AsMatch

bit_avatar_switch = 0  # Активен ли модуль BitAvatar

read_on_switch = 0  # Активен ли модуль ReadOn

sending_me_switch = 0  # Активен ли модуль SendingMe
# Количество эфира, посылаемое на адрес контракта
sending_me_eth_value = [0.00000001, 0.000003]
sending_me_eth_digs = 8  # Знаков после запятой для эфира


# ///// Параметры для квестов Week 4
sarubol_mint_switch = 0  # Активен ли модуль Sarubol mint
zypher_2048_switch = 0  # Активен ли модуль Zypher 2048
lucky_cat_switch = 0  # Активен ли модуль LuckyCat


#       / Параметры старых модулей /
eth_swap_switch = 0  # Включен ли свап ETH на USDC перед операциями
usdc_swap_switch = 0  # Включен ли свап USDC на ETH после операций
# Количество USDC на которое будем свапать эфир перед операциями
usdc_volume = [1, 5]

#       / Параметры для работы скрипта /
# Запас эфира при переводе на адрес биржи и бридже (ETH), чтобы точно прошло
exc_remains = [0.000003, 0.000005]
rem_digs = 6  # Количество знаков после запятой для остатка на кошельке
test_mode = 0
last_row = 1
gas_price_ether = 999
stop_flag = False
start_flag = False
