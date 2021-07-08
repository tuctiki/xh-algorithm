"""
=======
旋转数组
=======
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


def basic(nums, k):
    if k == 0 or len(nums) == 0:
        return nums

    offset = k % len(nums)
    reversed_num = list(reversed(nums))

    return list(reversed(reversed_num[0:offset])) + list(reversed(reversed_num[offset:]))
