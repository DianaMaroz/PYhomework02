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

#без использования строковых методов, зато с использованием костылей

number_float = abs(float(input("Введите вещественное число: ")))
if int(number_float) > 0:
    while number_float - int(number_float) > 0:
        number_float *= 10
else:
    number_float += 1
    while number_float - int(number_float) > 0:
        number_float *= 10
    number_float -= 1
print(f'Сумма цифр числа {number} равна {int(sum_digit_for_int(number_float))}')


