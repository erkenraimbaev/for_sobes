def printing(function):
    def wrapper(*args, **kwargs):
        func = function(*args, **kwargs)
        print(func)
    return wrapper


list_not_unicaly = [1, 3, 3, 2]


@printing
def make_unicaly(*args):
    unicaly_set = set(args)
    return unicaly_set


make_unicaly(*list_not_unicaly)