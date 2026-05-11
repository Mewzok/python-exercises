def limited_activity_summary(actions):
    user_action_count = {}
    filtered_actions = {"logout"}

    for user, action in actions:
        if user != "admin" and action not in filtered_actions:
            if user_action_count.setdefault(user, 0) < 3:
                user_action_count[user] += 1

    return user_action_count

actions = [
    ("alice", "login"),
    ("alice", "view"),
    ("alice", "purchase"),
    ("alice", "comment"),
    ("bob", "view"),
    ("admin", "login"),
    ("bob", "logout")
]

print(limited_activity_summary(actions))