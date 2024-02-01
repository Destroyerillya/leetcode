def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n != 0 and m != 0:
        if nums1[m - 1] <= nums2[n - 1]:
            nums1[m + n - 1] = nums2.pop()
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            nums1[m - 1] = 0
            m -= 1
    if n != 0:
        nums1[0:n] = nums2[0:n]







nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)