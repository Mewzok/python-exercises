def longest_increase_streak(temps):
    previous_temp = None
    streak = 0
    max_streak = 0

    for temp in temps:
        if previous_temp is not None and temp > previous_temp:
            streak += 1

            if streak > max_streak:
                max_streak = streak
        else:
            streak = 0

        previous_temp = temp

    return max_streak

temps = [70, 72, 68, 75, 80, 78]

print(longest_increase_streak(temps))