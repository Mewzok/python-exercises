def most_frequent_user(usernames):
    top_user = None
    user_dictionary = {}

    for user in usernames:
        if user in user_dictionary:
            user_dictionary[user] += 1
            if user_dictionary[user] > user_dictionary[top_user]:
                top_user = user
        else:
            user_dictionary[user] = 1
            if top_user is None:
                top_user = user

    return top_user

usernames = ["alice", "bob", "charlie", "bob", "alice", "alice"]

print(most_frequent_user(usernames))