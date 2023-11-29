
# def removeDuplicates(nums: list[int]) -> int:
#     i = 1
#     previous_l = nums[0]
#     while i != len(nums):
#         if previous_l == nums[i]:
#             nums.pop(i)
#         elif previous_l != nums[i]:
#             previous_l = nums[i]
#             i += 1
#     return len(nums)

def removeDuplicates(nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)