# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

num = int(input("Введите целое число > 0: "))
my_list = []
for i in range(1, num + 1):
    my_list.append((1+1/i)**i)
sum_my_list = 0
for j in range(len(my_list)):
    sum_my_list += my_list[j]
print(*my_list)
print(sum_my_list)
