def count_actions(actions):
    counted_actions = {}

    # for action in actions:
    #     if action in counted_actions:
    #         counted_actions[action] += 1
    #     else:
    #         counted_actions[action] = 1

    for action in actions:
        counted_actions[action] = counted_actions.get(action, 0) + 1

    return counted_actions

actions = ["login", "view", "view", "logout", "login", "view"]

print(count_actions(actions))