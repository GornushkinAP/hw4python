# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
from random import randint

n = int(input("Введите количество элементов n: "))
m = int(input("Введите количество элементов m: "))

set1 = set()
set2 = set()

print("Введите по очереди элементы множества n :")
for i in range(n):
    element = int(input())
    set1.add(element)

print(set1)

print("Введите по очереди элементы множества m:")
for i in range(m):
    element = int(input())
    set2.add(element)

print(set2)

intersection = sorted(set1.intersection(set2))
print("Повторяющиеся числа по возрастанию:")
for num in intersection:
    print(num)
