



def lengthOfLastWord(s: str) -> int:
    length = 0
    for l in s[::-1]:
        if l == ' ' and length == 0:
            continue
        elif l == ' ' and length != 0:
            return length
        else:
            length += 1
    return length




#s = "luffy is still joyboy"
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))