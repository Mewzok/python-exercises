def purchase_totals(purchases):
    totals = {}

    for user, amount in purchases:
        if user not in totals:
            totals[user] = amount
        else:
            totals[user] = totals[user] + amount

    return totals

purchases = [
    ("alice", 20),
    ("bob", -5),
    ("alice", 30),
    ("bob", 15),
    ("alice", -10)
]

print(purchase_totals(purchases))

# 1. This function collects and returns a dictionary of individual users and the total sums of their purchases.
# 2. This function successfully fulfills its basic requirements.
# 3. A hypothetical approach to simplifying the function would be to replace the if-else block with a simple get() function, ex: totals[user] = totals.get(user, 0) + amount.