vote_box = []
label = "票"


def vote():
    print("投票します")
    vote_box.append(label)


def reset_box():
    print("箱を空にします")
    vote_box.clear()


def check_box():
    print("票の数は {} です".format(len(vote_box)), end=" ")
    print("vote_box:", vote_box)


# test


print(vote())
print(check_box())
print(vote())
print(check_box())
for i in range(3):
    vote()
print(check_box())
print(reset_box())
print(check_box())
