def activity_report(user_activities):
    activity_dict = {"total_actions": 0, "most_active_user": None, "action_count": 0}
    user_dict = {}

    for user, activity in user_activities:
        activity_dict["total_actions"] += 1
        
        user_dict[user] = user_dict.get(user, 0) + 1

        if activity_dict["most_active_user"] is None or user_dict[activity_dict["most_active_user"]] < user_dict[user]:
            activity_dict["most_active_user"] = user

    activity_dict["action_count"] = user_dict[activity_dict["most_active_user"]]
    return activity_dict

user_activities = [
    ("alice", "login"),
    ("bob", "view"),
    ("alice", "logout"),
    ("alice", "view"),
    ("bob", "view"),
    ("charlie", "login")
]

print(activity_report(user_activities))