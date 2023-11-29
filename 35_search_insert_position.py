
def searchInsert(nums: list[int], target: int) -> int:
    if nums[0] == target or nums[0] > target:
        return 0
    elif nums[len(nums) - 1] == target:
        return len(nums) - 1
    elif nums[len(nums) - 1] < target:
        return len(nums)

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = nums[mid]
        next_val = nums[mid + 1]
        previous_val = nums[mid - 1]
        if previous_val == target:
            return mid - 1
        elif mid_val == target or (mid_val > target and previous_val < target):
            return mid
        elif next_val == target or (mid_val < target and next_val > target):
            return mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            low = mid + 1


nums = [1,2,3,4,5,6,7,8,9,10]
target =  3
print(searchInsert(nums, target))