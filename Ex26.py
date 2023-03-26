# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# Пример
# A = 3; B = 5 -> 243
# A = 2; B = 3 -> 8


def func(a: int, b: int):
    if b == 1:
        return a
    else:
        return func(a, b - 1) * a


num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))

print(func(num_a, num_b))
