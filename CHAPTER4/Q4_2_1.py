def numbers_to_weeks(num=0):
    weeks = ["水曜日", "木曜日", "金曜日", "土曜日", "日曜日", "月曜日", "火曜日"]
    if num == 0 or num == -7:
        return weeks[0]
    elif num == 1 or num == -6:
        return weeks[1]
    elif num == 2 or num == -5:
        return weeks[2]
    elif num == 3 or num == -4:
        return weeks[3]
    elif num == 4 or num == -3:
        return weeks[4]
    elif num == 5 or num == -2:
        return weeks[5]
    elif num == 6 or num == -1:
        return weeks[6]
    elif num > 7:
        return "来週"
    else:
        return "先週"
