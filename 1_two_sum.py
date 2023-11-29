nums = [150, 24, 79, 50, 88, 345, 3]
target = 200


def twoSum(nums: list[int], target: int) -> list[int]:
    '''First variant O(N^2)'''
    i = 0
    while i != len(nums):
        rest = target - nums[i]
        if rest in nums[i + 1:]:
            print([i, nums[i + 1:].index(rest) + i + 1])
        i += 1


def twoSum_2(nums: list[int], target: int) -> list[int]:
    '''Second variant O(N)'''
    dict = {}
    for i, n in enumerate(nums):
        if n in dict:
            return dict[n], i
        else:
            dict[target - n] = i