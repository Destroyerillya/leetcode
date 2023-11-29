def planner() -> int:
    task_count = int(input())
    if task_count % 2 != 0:
        return -1
    tasks = input().split()
    i = 0
    j = len(tasks) - 1
    first_pair = int(tasks[len(tasks) - 1]) + int(tasks[0])
    while i != (len(tasks) // 2) - 1 and j != (len(tasks) // 2):
        if int(tasks[i]) + int(tasks[j]) != first_pair:
            return -1
        i += 1
        j -= 1
    return first_pair

print(planner())


def palindrom_time_1() -> int:
    max_hours, max_minutes = 7584, 45679
    max_hours = int(max_hours)
    max_minutes = int(max_minutes)
    if max_hours > max_minutes:
        max_hours, max_minutes = max_minutes, max_hours
    max_digits = max(len(str(max_hours - 1)), len(str(max_minutes - 1)))
    counter = 0
    hour = 0
    a = []
    while hour < max_hours:
        new_minute = str(hour)[::-1]
        new_minute = new_minute + "0" * (max_digits - len(new_minute))
        new_hour = "0" * (max_digits - len(str(hour))) + str(hour)
        if int(new_minute) < max_minutes:
            a.append([new_hour, new_minute])
            counter += 1
        hour += 1
    for i in sorted(a):
        print(i[::-1])
    return counter


def palindrom_time_2() -> int:
    max_hours, max_minutes = "703", "3070"
    max_hours_int = int(max_hours)
    max_minutes_int = int(max_minutes)
    if max_hours > max_minutes:
        max_hours, max_minutes = max_minutes, max_hours
    max_digits = max(len(str(max_hours_int - 1)), len(str(max_minutes_int - 1)))
    counter = 0
    i = len(max_hours) - 1
    cur_hour = 0
    number = 1
    tens = 1
    next_len = 0
    while i != 0:
        new_minute = str(cur_hour)[::-1]
        new_minute = new_minute + "0" * (max_digits - len(new_minute))
        if cur_hour <= max_hours_int and int(new_minute) <= max_minutes_int:
            print(cur_hour)
            cur_hour += 1
            counter += 1
        elif cur_hour <= max_hours_int and int(new_minute) > max_minutes_int:
            if number <= 9:
                number += 1
            else:
                number = 1
                tens *= 10
                i -= 1
            cur_hour = str(number) + str(tens)
            cur_hour = int(cur_hour)
        elif cur_hour > max_hours_int:
            return counter



print(palindrom_time_1())
print(palindrom_time_2())
