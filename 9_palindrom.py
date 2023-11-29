x = 1


def isPalindrome(x: int) -> bool:
    '''First variant O(N)'''
    if x == 0:
        return True
    elif x < 0 or x % 10 == 0:
        return False
    else:
        return True if str(x) == str(x)[::-1] else False