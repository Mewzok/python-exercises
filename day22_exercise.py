def purchase_report(user_data):
    users = set()
    purchase_data = {"total_users": 0, "total_spent": 0, "highest_purchase": 0}

    for user, amount in user_data:
        if user not in users:
            users.add(user)
            purchase_data["total_users"] += 1
        
        purchase_data["total_spent"] += amount

        if amount > purchase_data["highest_purchase"]:
            purchase_data["highest_purchase"] = amount

    return purchase_data

user_data = [
    ("alice", 20),
    ("bob", 15),
    ("alice", 30),
    ("bob", 5),
    ("charlie", 50)
]

print(purchase_report(user_data))