#s = "{[([])]}"
# s = "){"
s = "()[]({[()]}){}"

def isValid_1(s: str) -> bool:
    if len(s) <= 1:
        return False

    if len(s) % 2 != 0:
        return False

    i = 0
    sub_s = ""

    while i != len(s):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            sub_s += s[i]
            i += 1
        elif (s[i] == ')' or s[i] == '}' or s[i] == ']') and sub_s == '':
            return False
        elif (sub_s[len(sub_s) - 1] == '(' and s[i] == ')') or (sub_s[len(sub_s) - 1] == '{' and s[i] == '}') or (sub_s[len(sub_s) - 1] == '[' and s[i] == ']'):
            sub_s = sub_s[0: len(sub_s) - 1]
            i += 1
        else:
            return False

    return sub_s != ""

def isValid_2(s):
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()]:
            return False
    return len(stack) == 0


print(isValid_2(s))