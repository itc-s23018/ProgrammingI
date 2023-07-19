def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        c = a + b
        result.append(c)
        a, b = b, c
    return result
