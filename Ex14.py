# Требуется вывести все целые степени двойки (т.е. числа 2 в степени k ), не превосходящие числа N

number = int(input("Введите число: "))

check_num = 1

while check_num <= number:
    print(check_num, end=" ")
    check_num *= 2

print(f"\n")
