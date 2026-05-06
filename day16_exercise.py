def total_spent_by_user(usernames):
    totals_dict = {}

    for user, money in usernames:
        totals_dict[user] = totals_dict.get(user, 0) + money

    return totals_dict

usernames = [
    ("alice", 20),
    ("bob", 15),
    ("alice", 30),
    ("bob", 5),
    ("charlie", 50)
]

print(total_spent_by_user(usernames))