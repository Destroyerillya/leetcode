word = "zzaaa"

def equalFrequency(word: str) -> bool:
    frequency = {}
    for l in word:
        frequency.setdefault(l, 0)
        frequency[l] += 1

    if len(frequency) == 1:
        return True

    list_numbers = []
    for key, value in frequency.items():
        list_numbers.append(value)

    if len(set(list_numbers)) > 2:
        return False

    all_ones = True
    count_ones = 0
    for i in list_numbers:
        if i != 1:
            all_ones = False
        else:
            count_ones += 1

    if all_ones:
        return True

    if count_ones == 1:
        return True

    first_value = min(list_numbers)
    counter = 0
    for i in list_numbers:
        if i != first_value:
            counter += 1

    if counter < 2:
        min_value = min(list_numbers)
        max_value = max(list_numbers)
        if max_value - min_value == 1:
            return True

    return False

print(equalFrequency(word))

# NN1
# 112
# 111