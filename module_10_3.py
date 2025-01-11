#!/home/igor/PycharmProjects/module_10/.venv/bin/python
# -*- coding: utf-8 -*-
import threading
from time import sleep
from random import randint
class Bank:
    def __init__(self):
        self.balance: int = 0  # баланс банка
        self.lock = threading.Lock()
    def deposit(self):
    # 100 циклов "пополнения" баланса
        for i in range(100):
            a = randint(50, 500)  # случайная сумма от 50 до 500
            self.balance += a  # пополнение баланса
            if self.balance >= 500 and self.lock.locked():
               self.lock.release()  # разблокирование баланса по условию
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        # 100 циклов "снятия" баланса
        for i in range(100):
            a = randint(50, 500)  # случайная сумма от 50 до 500
            print(f'Запрос на {a}')
# если списание меньше баланса, то снятие иначе запрос отклонен, блокировка
            if a < self.balance:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


