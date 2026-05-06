def top_spender_with_amount(users):
    totals_dict = {}
    current_most_money = None
    current_top_spender = None

    for user, money in users:

        totals_dict[user] = totals_dict.get(user, 0) + money

        if current_most_money is None or totals_dict[user] > current_most_money:
            current_top_spender = user
            current_most_money = totals_dict[user]

    return current_top_spender, current_most_money

users = [
    ("alice", 20),
    ("bob", 15),
    ("alice", 30),
    ("bob", 5),
    ("charlie", 50)
]

print(top_spender_with_amount(users))