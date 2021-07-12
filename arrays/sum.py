"""
=======
两数之和
=======
给定一个整数数组 nums 和一个目标值 target，请你在该
"""


def basic(nums, target):
    dict0 = {}
    i = 0
    while i < len(nums):
        if target - nums[i] in dict0.keys():
            return [dict0.get(target - nums[i]), i]
        else:
            dict0[nums[i]] = i
            i += 1
    return []
