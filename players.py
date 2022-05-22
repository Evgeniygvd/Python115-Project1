# модуль работы с данными игроков

from configparser import ConfigParser


PLAYER = tuple()
SAVES = {}
PLAYERS = {'oleg':[1,1,1]}

def field():
    global FIELD
    for i in range(len(FIELD)):
        print('-'*13)
        print('|',FIELD[i][0],'|',FIELD[i][1],'|',FIELD[i][2],'|')
    print('-'*13)


def save_ini():
    config = ConfigParser()
    config['Scores '] = {name: ',' .join(str(n) for n in score)
                         for name, score in PLAYERS.items()}
    config['Saves'] = {';'.join(name): ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['General']['first'] = 'no'
    with open('data.ini', 'w', enconding ='utf-8') as config_file:
        config.write(config_file)






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

def player_name(bot_mode=''):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input().lower(),)
    elif len(PLAYER) == 1:
        if bot_mode:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], input().lower())
        else:
            # Добавить имя второго игрока человека
            PLAYER = (PLAYER[0], input().lower())
    else:
        pass

