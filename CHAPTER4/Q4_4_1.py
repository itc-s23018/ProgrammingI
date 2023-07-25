vote_num = 0


def vote():
    print("投票します")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))


print(vote())
print(check_box())
print(vote())
print(check_box())
for i in range(3):
    print(vote())
print(check_box())
print(reset_box())
print(check_box())
