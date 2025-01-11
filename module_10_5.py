#!/home/igor/PycharmProjects/module_10/.venv/bin/python
# -*- coding: utf-8 -*-
import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
        all_data.extend(lines)

filenames = [f'./file {number}.txt' for number in range(1, 5)]


# Линейный вызов
start = datetime.datetime.now()
for name in filenames:
    read_info(name)
end = datetime.datetime.now()
print(end - start)

# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)