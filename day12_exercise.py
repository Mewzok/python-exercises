def username_exists(usernames, new_username):

#     for user in usernames:
#         if user == new_username:
#             return True

#     return False
    return new_username in usernames

usernames = ["alice", "bob"]
new_username0 = "bob"
new_username1 = "eve"

print(username_exists(usernames, new_username0))
print(username_exists(usernames, new_username1))