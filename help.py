# модуль работы со справкой

from shutil import get_terminal_size as gts
from math import floor, ceil

COMMANDS = {'quit': ('quit', 'выход'), 'help': ('help', 'помощь', 'h', '?'),
            'scores': ('scores', 'таблица'), 'new': ('new', 'новая', 'да', 'y', 'д'),}

MESSAGES = (' хотите начать новую партию? > ',
            ' введите имя игрока > ',
            ' введите имя второго игрока > ',
            ' выберите режим игры:\n 1 - c ботом\n - с человеком\n> ',
            ' выберите уровень сложности:\n 1- легкий\n - трудный\n> ',
            ' вы хотите ходить первым? >',
            ' вы хотите загрузить сохраненную партию'
            )

ANSWERS = (None,
           None,
           None,
           ('1', 'бот', 'б', '2', 'человек', 'ч'),
           ('1', 'легкий', 'л', '2', 'трудный', 'т'),
           ('yes', 'да', 'y', 'д'),
           ('yes', 'да', 'y', 'д'),
           )




h = """Правила игры:

    
Список команд:  
{' '.join(COMMANDS['quit'])}

    """



# функция демонстрации справки
def show_help():
    print(h)

# функция оформления текста
def show_message(text):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2) / 2
    m = (f"\n{'#' * width}"
         + f"\n{'#' + ' ' * (width - 2) + '#'}"
         + f"\n{'#' + ' ' * ceil(half_width) + text.upper() + ' ' * floor(half_width) + '#'}"
         + f"\n{'#' + ' ' * (width - 2) + '#'}"
         + f"\n{'#' * width}")
    print(m, end='\n\n')
