def add_purchase(users, username, amount):

    users.setdefault(username, {
        "total_spent": 0,
        "purchase_count": 0
    })

    users[username]["total_spent"] += amount

    if amount > 0:
        users[username]["purchase_count"] += 1

    return users

users = {
    "alice": {
        "total_spent": 50,
        "purchase_count": 2
    }
}

print(add_purchase(users, "alice", 20))