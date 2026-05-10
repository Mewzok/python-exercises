def valid_purchase_totals(purchases):
    user_totals = {}

    for user, purchase in purchases:
        if purchase is not None and purchase >= 0:
            user_totals[user] = user_totals.get(user, 0) + purchase

    return user_totals

purchases = [
    ("alice", 20),
    ("bob", -5),
    ("alice", 30),
    ("charlie", None),
    ("bob", 15),
    ("alice", -10)
]

print(valid_purchase_totals(purchases))