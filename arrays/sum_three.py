"""
=======
三数之和
=======
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。注意：答案中不可以包含重复的三元组。
"""


def basic(nums, target):
    nums.sort()
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                j = j + 1
            elif s > target:
                k = k -1
            else:
                return [nums[i], nums[j], nums[k]]
        i = i + 1
    return []
