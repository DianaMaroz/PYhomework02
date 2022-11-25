# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)
def shuffle_my_list(sm_list):
    new_list = []
    random_list = []
    for i in range(len(sm_list)):
        gen_index = random.randint(0, len(sm_list) - 1)
        while gen_index in random_list:
            gen_index = random.randint(0, len(sm_list) - 1)
        new_list.append(sm_list[gen_index])
        random_list.append(gen_index)
    return new_list

print(shuffle_my_list(my_list))


