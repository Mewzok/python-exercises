# def get_long_usernames(usernames):
#     long_usernames = []

#     for user in usernames:
#         if len(user) > 4:
#             long_usernames.append(user)

#     return long_usernames

def get_long_usernames(usernames):
    return [user for user in usernames if len(user) > 4]

usernames = ["alice", "bob", "charlie", "david", "eve"]

print(get_long_usernames(usernames))