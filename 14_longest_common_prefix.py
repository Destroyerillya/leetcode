strs = ["ab","a"]
# strs = ["dog","racecar","car"]


def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        if len(strs[0]) == 0:
            return ""
        else:
            return strs[0]
    if len(strs[0]) == 0:
        return ""
    j = 1
    dirty_flag = False
    i = 0
    while True:
        if not strs[i].startswith(strs[0][0:j]):
            if dirty_flag:
                return strs[0][0:j - 1]
            else:
                return ""
        i += 1
        if i == len(strs):
            if j == len(strs[0]):
                return strs[0]
            i = 0
            dirty_flag = True
            j += 1



print(longestCommonPrefix(strs))