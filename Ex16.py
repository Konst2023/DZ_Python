# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint

arr_len = int(input("Введите длину массива: "))
number = int(input("Введите число от 1 до 10: "))
num_list = [randint(1, 10) for _ in range(arr_len)]

counter = 0
for i in range(arr_len):
    if num_list[i] == number:
        counter += 1

print(num_list)
print(f"Число {number} повторяется {counter} раз")
