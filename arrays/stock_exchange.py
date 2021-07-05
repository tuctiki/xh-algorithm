"""
===============
买卖股票的最佳时机
===============
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。注意你不能在买入股票前卖出股票。
"""


def basic(nums):
    tmp = []
    i = 0
    profit = 0
    while i < len(nums):
        if len(tmp) > 0 and (i == len(nums) - 1 or (i < len(nums) - 1 and nums[i] >= nums[i + 1])):
            profit += (nums[i] - tmp[0])
            tmp.clear()
        elif i < len(nums) - 1 and nums[i] < nums[i + 1]:
            tmp.append(nums[i])
        i += 1
    return profit
