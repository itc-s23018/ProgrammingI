import random

alphabet = [chr(i) for i in range(97, 97 + 26)]
my_str = "t"

while True:
    random_str = random.choice(alphabet)
    print(random_str)
    if random_str == my_str:
        break
