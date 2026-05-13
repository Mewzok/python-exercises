def unique_activity_summary(actions):
    tracker = {}

    for user, action in actions:

        tracker.setdefault(user, [])
        
        if action not in tracker[user]:
            tracker[user].append(action)

    return { user: len(activities) for user, activities in tracker.items() }

actions = [
    ("alice", "login"),
    ("alice", "login"),
    ("alice", "view"),
    ("alice", "view"),
    ("bob", "view"),
    ("bob", "view"),
    ("charlie", "purchase")
]

print(unique_activity_summary(actions))