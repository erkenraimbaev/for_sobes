import re

with open('file.txt', mode='r') as f:
    # f.write('aaa')
    list_ = f.readlines()
    print(list_)
    str_ = (''.join(list_))
    # str__ = str_.replace('a', '***', len(str_))
    print(re.sub("^\s+|\n|\r|\s+$", '', str_))

