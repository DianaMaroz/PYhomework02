# TНапишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input("Введите число: ")
# с использованием строковых методов
number_int = int(number.replace('.', ''))
def sum_digit_for_int(num):
    dig_sum = 0
    while num > 0:
        dig_sum += num % 10
        num = num // 10
    return dig_sum

print(f'Сумма цифр числа {number} равна {sum_digit_for_int(number_int)}')

#без использования строковых методов
number_float = float(input("Введите вещественное число: "))


