def top_spender(users):
    totals_dict = {}
    current_most_money = int(users[0][1])
    current_top_spender = None

    for user, money in users:
        totals_dict[user] = totals_dict.get(user, 0) + money

        if totals_dict[user] > current_most_money:
            current_top_spender = user
            current_most_money = totals_dict[user]

    return current_top_spender

users = [
    ("alice", 20),
    ("bob", 15),
    ("alice", 30),
    ("bob", 5),
    ("charlie", 50)
]

print(top_spender(users))