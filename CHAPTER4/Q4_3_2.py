numbers = list(range(100))


def func_square(*args):
    result = []
    for n in args:
        result.append(n**2)
    return result


print(func_square(*numbers))
