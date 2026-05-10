def highest_spender(users):
    top_user = None

    for user in users:
        if top_user is None or users[top_user]["total_spent"] < users[user]["total_spent"]:
            top_user = user

    return top_user, users[top_user]["total_spent"]

users = users = {
    "alice": {
        "total_spent": 50,
        "purchase_count": 2
    },
    "bob": {
        "total_spent": 15,
        "purchase_count": 1
    },
    "charlie": {
        "total_spent": 100,
        "purchase_count": 4
    }
}

print(highest_spender(users))