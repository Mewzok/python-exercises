def activity_summary(actions):
    action_totals = {}
    untracked_actions = {"logout"}

    for user, action in actions:
        if action not in untracked_actions:
            action_totals[user] = action_totals.get(user, 0) + 1

    return action_totals

actions = [
    ("alice", "login"),
    ("bob", "view"),
    ("alice", "logout"),
    ("alice", "purchase"),
    ("bob", "logout"),
    ("charlie", "login")
]

print(activity_summary(actions))