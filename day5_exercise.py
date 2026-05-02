def average_warm_days(temps):
    temp_sum = 0
    temp_avg = 0
    count = 0

    for temp in temps:
        if temp > 70:
            temp_sum += temp
            count += 1

    if count > 0:
        temp_avg = temp_sum / count

    return temp_avg

temps = [72, 65, 80, 90, 60, 75]

temp_avg = average_warm_days(temps)

if temp_avg > 0:
    print(temp_avg)
else:
    print("No temperatures greater than 70.")
