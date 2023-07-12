my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
six_list = []

for i in my_list:
    if len(i) >= 6:
        six_list.append(i)
print(six_list)
