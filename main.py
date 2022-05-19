# модуль верхнего уровня для работы приложения

from players import *
from help import show_help, show_message


# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')


#импорты
from configparser import ConfigParser


#глобальные перменные




PLAYERS = {}
#PLAYERS = {'Ivan':[1,1,0]}
SAVES = {}
#SAVES = {('ivan','ai1'):[[]],
#         ('ivan','oleg'): [[]]}

#функции

#чтение .ini файла
if read_ini():
    show_help()

#запуск суперцикла
while True:
    command = input('_>')


    if command in ('quit','выход'):
        break

    elif command in ('new','новая', 'да'):
        # есть ли текущий игрок
        if not PLAYER:
            player_name()

#ввод имени игрока

