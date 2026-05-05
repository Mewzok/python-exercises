def group_users_by_color(user_colors):
    color_groups = {}

    for username, color in user_colors:
        color_groups.setdefault(color, []).append(username)

    return color_groups

user_colors = [
    ("alice", "red"),
    ("bob", "blue"),
    ("alice", "green"),
    ("bob", "red")
]

print(group_users_by_color(user_colors))