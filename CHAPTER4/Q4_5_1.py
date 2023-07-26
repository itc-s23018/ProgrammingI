functions = [sum, min, max]
nums = range(1, 11)
list(nums)

for func in functions:
    print("functions: {}, result: {}".format(func.__name__, func(nums)))
