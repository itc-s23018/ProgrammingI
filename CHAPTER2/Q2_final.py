import random

alphabet = [chr(i) for i in range(65, 65 + 26)]
my_str = "T"

while True:
    random_str = random.choice(alphabet)
    print(random_str)
    if random_str == my_str:
        break
