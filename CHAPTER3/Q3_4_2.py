numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0

for n in numbers:
    if n > 10:
        break  # １０以上なら停止
    x += n  # リストの１〜８まで足し算されていく
print(x)
