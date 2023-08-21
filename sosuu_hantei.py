def prime_number(n):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input())
if prime_number(num):
    print('素数')
else:
    print('素数ではありません')
