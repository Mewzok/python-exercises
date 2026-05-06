def count_increases(temps):
    previous_temp = None
    increase_count = 0

    for temp in temps:
        if previous_temp is not None and temp > previous_temp:
            increase_count += 1

        previous_temp = temp

    return increase_count

temps = [70, 72, 68, 75, 80, 78]

print(count_increases(temps))