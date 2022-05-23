from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:

    
Список команд:  


    """


# обязательно подписывать: что за функция и что делает
def show_help():
    print(h)

# обязательно подписывать: что за функция и что делает
def show_message(text):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2) / 2
    # можно ещё вот так определить строку
    m = (f"\n{'#' * width}"
         + f"\n{'#' + ' ' * (width - 2) + '#'}"
         + f"\n{'#' + ' ' * ceil(half_width) + text.upper() + ' ' * floor(half_width) + '#'}"
         + f"\n{'#' + ' ' * (width - 2) + '#'}"
         + f"\n{'#' * width}")
    print(m, end='\n\n')
