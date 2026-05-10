def count_logins(actions):
    counts = {}

    for user, action in actions:
        if action == "login":
            counts[user] = counts.get(user, 0) + 1

    return counts

# 1. This function counts the number of logins per user.
# 2. The dictionary stores the user's username and the count of their logins.
# 3. This line creates a key within the dictionary "counts" named for the current user in the loop with the value 0 if one does not exist. Regardless of whether it existed or not, it will then return the value, allowing it to be modified with the +1, increasing it by 1. It will then finally assign this result to the value in the either previously existing or newly created counts[user].
# 4. For the given values, this function would return 'alice': 2. This is because Alice made a login action twice, and so she would be stored in the dictionary and have her key's value incremented twice. Bob did not make a login action, thus the if statement's condition is never met, so Bob would not have a key/value created in the dictionary.

# Results/Personal notes: counts.get(user, 0) + 1 does not create the key/value pair, the counts[user] part does. I internally knew this as I remember specifically internalizing how .get() is entirely read only when learning about it, but totally blanked on that when writing the answer. Or maybe I just mashed everything together in my head? Regardless, big mistake to learn from and need to be more careful in the future. Additionally, pay close enough to what is specifically returned. I responded with 'alice': 2, which is close, but in this function return specifically returned the entire dictionary, meaning the printed result would be {'alice': 2}. Again, seemingly minor distinction but these details could make or break me. Need to be better.