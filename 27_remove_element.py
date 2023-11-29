

def removeElement(nums: list[int], val: int) -> int:
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)





nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

removeElement(nums, val)
print(nums)