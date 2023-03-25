# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

num1 = int(input("Введите длину набора целых чисел 1 "))
num2 = int(input("Введите длину набора целых чисел 2 "))

list1 = [randint(0, 10) for _ in range(num1)]
list2 = [randint(0, 10) for _ in range(num2)]
print(list1)
print(list2)

set1 = set(list1)
set2 = set(list2)

inter_set = set1.intersection(set2)  # пересечение
inter_set = sorted(inter_set)  # сортировка, на выход список

print(inter_set)