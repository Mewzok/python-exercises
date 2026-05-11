def valid_purchase_summary(purchases):
    totals = {}

    for user, amount in purchases:
        valid_user = user != "admin" 
        valid_amount = amount is not None and amount > 0

        if valid_user and valid_amount:
            totals[user] = totals.get(user, 0) + amount

    return totals

purchases = [
    ("alice", 20),
    ("bob", None),
    ("admin", 100),
    ("alice", -5),
    ("bob", 15),
    ("charlie", 50)
]

print(valid_purchase_summary(purchases))