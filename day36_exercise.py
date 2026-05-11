def filtered_activity_summary(actions):
    user_action_count = {}
    filtered_actions = {"logout"}

    for user, action in actions:
        if user != "admin" and action not in filtered_actions:
            user_action_count[user] = user_action_count.get(user, 0) + 1

    return user_action_count

actions = [
    ("alice", "login"),
    ("admin", "view"),
    ("alice", "purchase"),
    ("bob", "logout"),
    ("bob", "view"),
    ("admin", "logout")
]

print(filtered_activity_summary(actions))