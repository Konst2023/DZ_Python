# Найдите сумму цифр трехзначного числа.
number = int(input("Введите трехзначное число: "))

num_sum = 0

while number > 0:
    fig = number % 10
    number = number // 10
    num_sum += fig

print(f"Сумма входящих чисел = {num_sum}")
