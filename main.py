# модуль верхнего уровня для работы приложения

from players import *
from help import show_help, show_message, MESSAGES, COMMANDS
from field import game

# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')

# чтение .ini файла
if read_ini():
    show_help()

# запуск суперцикла
while True:
    command = input(MESSAGES[0]).lower()


    # выход из программы
    if command in COMMANDS['quit']:
        # обработка завершения работы приложения
        break
    # показать справку
    elif command in COMMANDS['help']:
        show_help()
    # показать таблицу результатов
    elif command in COMMANDS['scores']:
        pass
    # начало новой партии
    elif command in COMMANDS['new']:
        # есть ли текущий игрок
        if not PLAYER:
            # запрос имени игрока
            player_name()

        if game_mode():
            # продолжаем сохраненную партию
            game(load=True)
        else:
            # начинаем новую партию
            pass
        # после завершения партии выводится статистика для участвовавших игроков






