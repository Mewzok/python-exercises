def count_actions(actions):
    counts = {}
    allowed_actions = {"login", "view"}

    for user, action in actions:
        if action in allowed_actions:
            counts[user] = counts.get(user, 0) + 1

    return counts

actions = [
    ("alice", "login"),
    ("alice", "logout"),
    ("bob", "view"),
    ("alice", None),
    ("charlie", "error"),
    ("bob", "view")
]

print(count_actions(actions))