def count_users(usernames):
    counts = {}

    for name in usernames:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

    return counts

usernames = ["alice", "bob", "alice", "eve", "bob", "alice"]

print(count_users(usernames))