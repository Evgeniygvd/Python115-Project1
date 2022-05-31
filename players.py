# модуль работы с данными игроков

from configparser import ConfigParser
from help import MESSAGES, ANSWERS
from field import check_saves

SCORES = {}
# SCORES = {'oleg':[1, 1, 1]}
PLAYER = tuple()
# PLAYER = ('ivan','ai1')

SAVES = {}


# сохранить в конфигурационный файл статистику игроков и их сохранения
def save_ini():
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        # статистику побед записываем для каждого игрока в виде строки
        config['Scores '] = {name: ',' .join(str(n) for n in score)
                         for name, score in SCORES.items()}
        # из матрицы поля формируем строку для хранения в конфигурационном файле
        config['Saves'] = {';'.join(name): ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
        # если сохраняем данные, значит следующий запуск будет уже не первым
        config['General']['first'] = 'no'
        with open('data.ini', 'w', encoding='utf-8') as config_file:
            config.write(config_file)

# читать из конфигурационного файла статистику игроков и их сохранения
def read_ini():
    global SCORES, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        # статистика побед хранится в виде строки - делаем из нее список чисел
        SCORES = {name.title(): [int(n) for n in score.split(',')]
                  for name, score in config['Scores'].items()}
         # сохранение партии хранится в виде строки - формируется матрица поля
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i+3]]
                      for i in range(0, 9, 3)]
                 for name, field in config['Saves'].items()}
        # первый запуск приложения
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

# принять на вход имя пользователя или добавить бота или изменить очередность хода
def player_name(bot_mode='', *, change_order = False):
    global PLAYER
    # ввод имени первого игрока
    if len(PLAYER) == 0:
        PLAYER = (input(MESSAGES[1]).lower(),)
    # ввод имени второго игрока
    elif len(PLAYER) == 1:
        # в этот параметр необходимо передать строку 'ai1' или 'ai2'
        if bot_mode:
            # добавить бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        # а если в параметре значение по умолчанию '', то добавляем имя второго человека
        else:
            # ввести имя второго игорка человека
            PLAYER = (PLAYER[0], input(MESSAGES[2]).lower())
    else:
        pass
    if change_order:
        PLAYER = (PLAYER[1], PLAYER[0])

# запросить у пользователя режим игры
def game_mode():
    global PLAYER
    # выбор режима игры
    while True:
        gm = input(MESSAGES[3]).lower()
        if gm in ANSWERS[3]:
            break
    # в случае одиночной игры
    if gm in ANSWERS[3][:3]:
        # есть ли сохранение для одиночной игры
        if save := check_saves():
            # восстановление уровня сложности и очередности хода из сохраненной партии
            PLAYER = save
            return True
        # запрос уровня сложности
        while True:
            dl = input(MESSAGES[4]).lower()
            if dl in ANSWERS[4]:
                break
        # добавляем имя бота к PLAYER
        if dl in ANSWERS[4][:3]:
            dl = 'ai1'
        else:
            dl = 'ai2'
        player_name(dl)
    # в случае парной игры
    else:
        player_name()
        if save := check_saves(single = False):
            # восстановление уровня сложности и очерёдности хода из сохранённой партии
            PLAYER = save
            return True


    # выбор очередности хода
    if not (input(MESSAGES[5]).lower() in ANSWERS[5]):
        player_name(change_order = True)

# вывод статистики или таблицы результатов
def show_stat():
    pass




# здесь должна быть функция или функции работы со статистикой
