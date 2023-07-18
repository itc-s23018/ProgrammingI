import random

numbers = [str(i) for i in range(0, 10)]
num4 = "".join(random.sample(numbers, k=4))

while True:
    val = input()
    if val == num4:
        break
    if len(val) != 4:
        print("4つの数字を入力してください。")
        continue
    answer = ""
    X_count = 0

    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += "X"
            X_count += 1

    remaining_count = X_count
    print("-> " + answer + '\n' + "あと" + str(remaining_count) + "個で正解です")

