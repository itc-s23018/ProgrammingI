with open("number.txt", "r") as f:  # with open()でファイルを開く。ファイル名はfにする
    sum = 0  # 変数sumを初期化
    for data in f:  # fの要素をfor文で変数dataに入れる。
        num = int(data)  # dataをintに変換し、変数numに入れる。
        sum += num  # 変数numを変数sumに追加
    print(sum)
