my_list = []

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{result:2d}", end=" ")
        if j % 9 == 0:
            print()
