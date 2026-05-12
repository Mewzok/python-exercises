def cleaned_activity_summary(actions):
    counts = {}
    filtered_users = {"", "admin"}
    filtered_actions = {"logout"}

    for user, action in actions:
        if user not in filtered_users and action not in filtered_actions:
            counts[user] = counts.get(user, 0) + 1

    return counts

actions = [
    ("alice", "login"),
    ("", "view"),
    ("admin", "purchase"),
    ("bob", "logout"),
    ("charlie", "view"),
    ("", "logout")
]

print(cleaned_activity_summary(actions))