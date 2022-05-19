# модуль верхнего уровня для работы приложения

from players import *
from help import show_help

# приветствие


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
    command = input()


    if command in ('quit','выход'):
        break

    #ввод имени игрока

