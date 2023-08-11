# Создайте функцию, которая создаёт файлы с указанным расширением. 
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint, choice
import os
os.system('cls')

LETTERS = 'eyuioaqwrtpsdfghjklzxcvbnm'

def filename_gen(min_len_name: int, max_len_name: int) -> str:
    res_word = ''
    for _ in range(randint(min_len_name, max_len_name)):
        res_word += choice(LETTERS)
    return res_word

def create_file(ext: str,
            min_len_name: int = 6, 
            max_len_name: int = 30,
            min_quant_bytes: int = 256,
            max_quant_bytes: int = 4096, 
            quantity_files: int = 42):
    
    for _ in range(quantity_files):
        with open(filename_gen(min_len_name, max_len_name) + ext, 'wb') as f:
            f.write(os.urandom(randint(min_quant_bytes, max_quant_bytes)))
    
ext = '.txt'
min_len_name = 3
max_len_name = 10
min_quant_bytes = 8
max_quant_bytes = 16
quantity_files = 3

if __name__ == '__main__':
    create_file(ext, min_len_name, 
         max_len_name, min_quant_bytes, 
         max_quant_bytes, quantity_files)

