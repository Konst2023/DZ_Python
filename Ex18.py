# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
from random import randint

arr_len = int(input("Введите длину массива: "))
number = int(input("Введите число от 1 до 10: "))
num_list = [randint(1, 10) for _ in range(arr_len)]
num_list = set(num_list)
num_list.discard(number)  # удаляем искомое число, если оно есть
num_list = list(num_list)

min = 11
close_num = 0
for i in range(len(num_list)):
    delta = abs(num_list[i] - number)
    if delta < min:
        min = delta
        close_num = num_list[i]

print(num_list)
print(f"Самое близкое число к числу {number} это {close_num}")
