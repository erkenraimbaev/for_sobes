list_gen = list((x * 10 for x in range(1, 5)))
print(list_gen)

list_gen1 = [x * 10 for x in range(1, 5)]
print(list_gen1)

print(list_gen == list_gen1)
print(list_gen is list_gen1)

keys = [1, 2, 3, 4, 5, 6, 7]
values = (1, 2, 3, 4, 5, 6)

# dict_gen = {k: v for k, v in zip(keys, values)}
dict1 = dict(zip(keys, values))
# print(dict1.__getitem__())
# print(dict_gen)

set_gen = set(x * 10 for x in range(1, 5))

tuple_gen = tuple(x * 10 for x in range(1, 5) if x % 2 == 0)
print(tuple_gen)


