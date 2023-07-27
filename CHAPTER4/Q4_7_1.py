def make_addfunc():
    def add(x, y):
        return x + y

    return add


adder = make_addfunc()
print(adder(1, 10))
