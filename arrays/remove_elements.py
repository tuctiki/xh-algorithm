"""
=======
移除元素
======
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
"""


def basic(nums, remove):
    i = 0
    while i < len(nums):
        if nums[i] == remove:
            nums = nums[0:i] + nums[i + 1:]
        else:
            i += 1
    return len(nums)


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次。
"""


def sored(nums, remove):
    i = 0
    while i < len(nums) and nums[i] <= remove:
        if nums[i] == remove:
            nums = nums[0:i] + nums[i + 1:]
        else:
            i += 1
    return len(nums)
