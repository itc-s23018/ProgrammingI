a = {x for x in "abcabcabc" if x not in "ab"}  # aは{'c'}が出力されている
b = {y for y in "abcabcabc" if y not in "bc"}  # bは{'a'}が出力されている
print(a | b)  # {'c'} + {'a'} になっていることによって答えは①
