print([x * y for x in range(3) for y in range(x + 1)])

# ① 0 * 0 = 0
# ② 1 * 0 = 0
# ③ 1 * 1 = 1
# ④ 2 * 0 = 0
# ⑤ 2 * 1 = 2
# ⑥ 2 * 2 = 4
# と計算の結果をリストにまとめたら [0, 0, 1, 0, 2, 4]となるので答えは③
