def func_square(*args):
    result = []
    for n in args:
        result.append(n * n)
    return result


numbers = list(range(100))
print(func_square(*numbers))
