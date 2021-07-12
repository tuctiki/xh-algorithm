"""
===
加一
===
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
"""


def basic(nums):
    i = len(nums) - 1
    while i >= 0:
        if nums[i] != 9:
            nums[i] += 1
            break
        else:
            nums[i] = 0
            i -= 1
    if i == -1 and len(nums) > 0:
        nums.insert(0, 1)
    return nums
