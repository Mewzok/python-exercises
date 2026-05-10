def purchase_summary(purchases):
    users = {}

    for user, purchase in purchases:
        if purchase is not None and purchase > 0:
            users.setdefault(user, {
                "total_spent": 0, "purchase_count": 0
            })
            users[user]["total_spent"] += purchase
            users[user]["purchase_count"] += 1

    return users

purchases = [
    ("alice", 20),
    ("bob", -5),
    ("alice", 30),
    ("charlie", None),
    ("bob", 15),
    ("alice", -10)
]

print(purchase_summary(purchases))