def unique_purchase_totals(purchases):
    totals = {}
    seen_purchases = {}

    for user, amount in purchases:

        totals.setdefault(user, 0)
        seen_purchases.setdefault(user, set())

        if amount is not None and amount > 0:
            if amount not in seen_purchases[user]:
                totals[user] += amount
                seen_purchases[user].add(amount)

    return totals

purchases = [
    ("alice", 20),
    ("alice", 20),
    ("alice", 30),
    ("bob", None),
    ("bob", 15),
    ("bob", 15),
    ("charlie", -5),
    ("charlie", 50)
]

print(unique_purchase_totals(purchases))