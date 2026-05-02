def find_first_long_username(usernames):
    long_user = ""

    for user in usernames:
        if len(user) > 5:
            return user

    return None

usernames = ["amy", "bob", "charlie", "dan"]

long_user = find_first_long_username(usernames)

if long_user != None:
    print(long_user)
else:
    print("No username over 5 letters.")
