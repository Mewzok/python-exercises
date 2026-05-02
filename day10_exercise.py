def find_max_and_count(temps):
    max_temp = temps[0]
    temp_count = 1

    for temp in temps:
        if temp > max_temp:
            max_temp = temp
            temp_count = 1
        elif temp == max_temp:
            temp_count += 1

    return max_temp, temp_count

example_temps_0 = [72, 85, 90, 67, 88]
example_temps_1 = [72, 90, 85, 90, 88]
example_temps_2 = [-5, -10, -3]

print(find_max_and_count(example_temps_2))