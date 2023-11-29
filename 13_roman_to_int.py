def romanToInt(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    previous_l = None
    summ = 0
    for l in s:
        if previous_l and roman_dict[l] > roman_dict[previous_l]:
            summ -= roman_dict[previous_l]
            summ += roman_dict[l] - roman_dict[previous_l]
        else:
            summ += roman_dict[l]
        previous_l = l
    return summ

romanToInt("MCMXCIV")