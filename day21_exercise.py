def count_valid_actions(user_actions):
    action_counts = {}

    for user, action in user_actions:
        if action is not None:
            action_counts[user] = action_counts.get(user, 0) + 1

    return action_counts

user_actions = [
    ("alice", "login"),
    ("bob", None),
    ("alice", "view"),
    ("charlie", "login"),
    ("bob", "view"),
    ("alice", None)
]

print(count_valid_actions(user_actions))