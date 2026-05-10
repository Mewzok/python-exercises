def count_views(actions):
    counts = {}

    for user, action in actions:
        if action == "view":
            counts[user] = counts.get(user, 0) + 1

    return counts

actions = [
    ("alice", "view"),
    ("alice", "view"),
    ("bob", "view")
]

print(count_views(actions))

# 1. The bug is that the function only returns values of 1 for each user key.
# 2. The bug happens because when the if statement condition is met, the function successfully creates a key for the user if one does not exist, but then exclusively assigns its value to 1. It doesn't increment, it only assigns to 1. counts[user] = 1 will always just assign the value to 1.
# 3. I believe the optimal fix would be to replace this line: counts[user] = 1 to this line: counts[user] = counts.get(user, 0) + 1. This should ensure that when the if statement condition is met, the user key is created as before, but now the value will be obtained if it exists prior and incremented by 1, and if not, it will be assumed as 0 and then incremented by 1, and either way, added as the value to the user key, successfully producing the desired result.

# 4. Result/Personal notes: Success. The only feedback was explaining to me that .get() does not create the key/value pair itself, which I of course know, but I suppose I worded it incorrectly in my answer. Will have to learn how to better word/express my thoughts.