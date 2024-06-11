file = open('dict.json', mode='a')
# dict_data = {'a': 100500, 'b': 200500}
dict_data = 'fff'


class MyError(BaseException):
    def __init__(self, text):
        # print('It is not dictionary!')
        self.text = text
        print(self.text)



try:
    if type(dict_data) is not dict:
        raise MyError('Not right')
    for i, k in dict_data.items():
        file.write(f'"{i}": {k},\n')
except TypeError:
    print('Object is not iterable')
except Exception:
    print('Use another data')
else:
    print('Adding to file')
finally:
    print('Close the file')
    file.close()
