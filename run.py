import sys
import logging


logging.basicConfig(level='INFO')
file_path = 'yumemi.log'
sys.stdout = open(file_path, "w")


from yumemiBot import yumemi

if __name__ == '__main__':
    yumemi.run()
    
