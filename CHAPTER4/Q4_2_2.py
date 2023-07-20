def perrin(m=100):
    a, b, c = 3, 0, 2
    perrin_list = []
    while a < m:
        perrin_list.append(a)
        a, b, c = b, c, a + b
    return perrin_list
