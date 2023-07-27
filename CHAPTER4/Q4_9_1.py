# 悪い例
spam( ham[ 1 ], { eggs: 2 })
# 正しい例
spam(hem[1], {eggs: 2})

# 悪い例
foo= (0, )
# 正しい例
foo = (0)

# 悪い例
if x == 4 : print (x , y) ; x , y = y , x
# 正しい例
if x == 4: print(x, y); x, y = y, x
