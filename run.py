import sys
from yumemiBot import yumemi


if __name__ == '__main__':
    
    file_path = 'yumemi.log'
    sys.stdout = open(file_path, "w")

    bot = yumemi
    bot.run()
    
