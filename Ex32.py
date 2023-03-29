# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint

num = int(input("Введите кол-во элементов списка: "))
left_bound = int(input("Значение левой границы: "))
right_bound = int(input("Значение правой границы: "))

num_list = [randint(-50, 50) for i in range(num)]
num_index = []
print(num_list)

for i in range(num):
    if left_bound <= num_list[i] <= right_bound:
        num_index.append(i)

print(num_index)
