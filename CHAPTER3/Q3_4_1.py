for i in range(10):
    if i % 2 == 0:
        continue  # 偶数ならスキップされる
    print(i)

for i in range(10):
    if i % 2 == 0:
        break  # 偶数なら停止される
    print(i)
