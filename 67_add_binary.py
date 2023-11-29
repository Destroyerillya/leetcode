# def addBinary(a: str, b: str) -> str:
#     summ = ""
#     i = -1
#     j = -1
#     rest = None
#     if len(a) < len(b):
#         a = (len(b) - len(a)) * "0" + a
#     if len(b) < len(a):
#         b = (len(a) - len(b)) * "0" + b
#     while abs(i) != len(a) + 1 and abs(j) != len(b) + 1:
#         if a[i] == b[i] == "1" and rest:
#             summ = "1" + summ
#         elif a[i] == b[i] == "1" and not rest:
#             summ = "0" + summ
#             rest = "1"
#         elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and rest:
#             summ = "0" + summ
#             rest = "1"
#         elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and not rest:
#             summ = "1" + summ
#         elif a[i] == b[i] == "0" and rest:
#             summ = "1" + summ
#             rest = None
#         elif a[i] == b[i] == "0" and not rest:
#             summ = "0" + summ
#         i -= 1
#         j -= 1
#     if rest:
#         summ = "1" + summ
#     return summ

def addBinary(a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2

    return ''.join(reversed(s))

a = "1010"
b = "1011"
print(addBinary(a,b))