def group_colors_by_user(user_colors):
    user_groups = {}

    for username, color in user_colors:
        if username in user_groups:
            user_groups[username].append(color)
        else:
            user_groups[username] = [color]
        
    return user_groups

user_colors = [
    ("alice", "red"),
    ("bob", "blue"),
    ("alice", "green"),
    ("bob", "red")
]

print(group_colors_by_user(user_colors))