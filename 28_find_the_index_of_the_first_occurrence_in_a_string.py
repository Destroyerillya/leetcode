# def strStr(haystack: str, needle: str) -> int:
#     if needle in haystack:
#         i = 0
#         while i != len(haystack):
#             if haystack[i: len(needle) + i] == needle:
#                 return i
#             i += 1
#     else:
#         return -1

def strStr(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0
    if len(needle) > len(haystack):
        return -1
    i, j = 0, 0
    dirty_i = None
    while i != len(haystack):
        if haystack[i] == needle[j]:
            if not dirty_i:
                dirty_i = i + 1
            i += 1
            j += 1
            if j == len(needle):
                return dirty_i - 1
        else:
            if j != 0:
                i = dirty_i
                dirty_i = None
                j = 0
            else:
                i += 1
    if dirty_i and j == len(needle):
        return dirty_i - 1
    return -1


haystack = "mississippi"
needle = "issipi"

print(strStr(haystack, needle))