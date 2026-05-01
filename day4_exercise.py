def find_highest_temperature(temps):
    max_temp = temps[0]

    for temp in temps:
        if temp > max_temp:
            max_temp = temp

    return max_temp

temps = [72, 85, 90, 67, 88]

print(find_highest_temperature(temps))