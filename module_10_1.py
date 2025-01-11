#!/home/igor/PycharmProjects/module_10/.venv/bin/python
# -*- coding: utf-8 -*-
import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово № {word} \n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = datetime.now()
result = finish - start
print(f'Работа функций:  {result}')

start = datetime.now()
t1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

finish = datetime.now()
result = finish - start
print(f'Работа потоков:  {result}')

