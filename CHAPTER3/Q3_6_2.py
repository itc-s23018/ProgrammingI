import random

numbers = [str(i) for i in range(0, 10)]
num4 = "".join(random.sample(numbers, k=4))
while True:
    val = input()
    if val == num4:
        break
    if len(val) != 4:
        print("input 4 numbers. ")
        continue
    answer = ""
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += "X"
    print("->" + answer)
