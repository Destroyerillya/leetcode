def plusOne(digits: list[int]) -> list[int]:
    full_num = 0
    counter = 1
    for digit in digits[::-1]:
        full_num += digit * counter
        counter *= 10
    return [int(digit) for digit in str(full_num + 1)]


digits = [1, 2, 3]
print(plusOne(digits))