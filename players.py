# модуль работы с данными игроков

from configparser import ConfigParser

PLAYERS = {'oleg':[1,1,1]}
PLAYER = tuple()

SAVES = {}


# обязательно подписывать: что за функция и что делает
def field():
    global FIELD
    for i in range(len(FIELD)):
        print('-'*13)
        print('|',FIELD[i][0],'|',FIELD[i][1],'|',FIELD[i][2],'|')
    print('-'*13)

# обязательно подписывать: что за функция и что делает
def save_ini():
    config = ConfigParser()
    config['Scores '] = {name: ',' .join(str(n) for n in score)
                         for name, score in PLAYERS.items()}
    config['Saves'] = {';'.join(name): ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['General']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)

# обязательно подписывать: что за функция и что делает
def read_ini():
    global PLAYERS, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding ='utf-8'):
        PLAYERS = {name: [int(n) for n in score.split(',')]
                   for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')): [[' ' if c == '-' else c for c in field[i:i+3]]
                                          for i in range(0,9,3)]
                 for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

# обязательно подписывать: что за функция и что делает
def player_name(bot_mode=''):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input('введите имя игрока_> ').lower(),)
    elif len(PLAYER) == 1:
        # если функции передан аргумент, значит нужно добавить бота
        if bot_mode:
            # имя бота берётся не из пользовательского ввода, а из параметра функции
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        # а если в параметре значение по умолчанию '', то добавляем имя второго человека
        else:
            PLAYER = (PLAYER[0], input('введите имя второго игрока_> ').lower())
    else:
        pass

# здесь должна быть функция или функции работы со статистикой
