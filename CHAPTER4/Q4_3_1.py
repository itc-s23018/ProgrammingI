def concat_words(*args, separator=","):
    return separator.join(args)


s = concat_words("沖縄県", "中頭郡", "読谷村字座喜味", separator=",")
print(s)
