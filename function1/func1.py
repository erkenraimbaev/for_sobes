def sum_numbers(a, b, c):
    result = a + b + c
    return result


print(sum_numbers(*[1, 2, 3]))

list_not_unicaly = [1, 3, 3, 2]
data_dict = {"name": "Ivan", "surname": "Ivanov", "age": 23}


list1 = sorted(list_not_unicaly, key=lambda x: x)
number_list = tuple(lambda x: x for x in range(1, 10))
even_numbers = list(filter(lambda x: x % 2 == 0, list_not_unicaly))
title_keys = list(map(lambda x: x.title(), data_dict.keys()))
# sum_of_numbers = reduce((lambda x, y: x + y), list_not_unicaly)
print(list1)
for i in number_list:
    print(i)
print(title_keys)


def make_unicaly(*args):
    unicaly_set = set(args)
    return unicaly_set


def get_values(**kwargs):
    number = 1
    values_list = kwargs.values()
    for value in values_list:
        print(f'{number}:{value}')
        number += 1


make_unicaly(*list_not_unicaly)
get_values(**data_dict)
