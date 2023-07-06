w = "○ "
b = "● "
answer = ""
for i in range(4):
    row = (w if i == j else b for j in range(4))
    answer += "".join(row) + "\n"
print(answer)
