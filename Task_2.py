# Доработаем предыдущую задачу. 
# Создайте новую функцию которая генерирует файлы с разными расширениями. 
# Расширения и количество файлов функция принимает в качестве параметров. 
# Количество переданных расширений может быть любым. 
# Количество файлов для каждого расширения различно. 
# Внутри используйте вызов функции из прошлой задачи.

from random import randint
from Task_1 import create_file
import os
os.system('cls')

def dif_ext_create_file(extensions: list, quantity_files: int):    
    for _ in range(quantity_files):
        current_ext = extensions[randint(0, len(extensions) - 1)]
        create_file(current_ext, 1)

if __name__ == '__main__':
    extensions = ['.txt', '.md', '.doc', '.log']
    quantity_files = 5  
    dif_ext_create_file(extensions, quantity_files)