# модуль верхнего уровня для работы приложения

from players import *
from help import show_help, show_message


# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')


# импорты
from configparser import ConfigParser


# глобальные перменные




PLAYERS = {}
# PLAYERS = {'Ivan':[1,1,0]}
SAVES = {}
# SAVES = {('ivan','ai1'):[[]],
#         ('ivan','oleg'): [[]]}

# функции

# чтение .ini файла
if read_ini():
    show_help()

# запуск суперцикла
while True:
    command = input('_>')


    if command in ('quit', 'выход'):
        break

    elif command in ('new', 'новая', 'да'):
        # есть ли текущий игрок
        if not PLAYER:
            player_name()

    # ввод имени игрока
    players_qty = int(input(f'Введите количество игроков'))
    if players_qty == 1:
        player1 = input(f'Введите имя игрока 1\n')
        if player1 in PLAYERS:
            pass
        else:
            PLAYERS[player1] = [0, 0, 0]
    elif players_qty == 2:
        player1, player2 = input(f'Введите имя игрока 1\n'), input(f'Введите имя игрока 2\n')
        if player1 in PLAYERS:
            pass
        else:
            PLAYERS[player1] = [0, 0, 0]
        if player2 in PLAYERS:
            pass
        else:
            PLAYERS[player2] = [0, 0, 0]
    else:
        print(f'Количество игроков не может быть больше двух')
        pass
