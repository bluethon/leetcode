#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 边界
        # #1 小于!不是大于
        if len(nums) < 3:
            return []
        # 排序, 利于后面去重
        nums.sort()
        # set排除重复值
        res = set()
        for i, x in enumerate(nums):
            # 如果i的值x等于i-1, 说明此值之前已经计算过, 跳过
            # #1 漏掉了, 注意判断i值
            if i >=1 and x == nums[i-1]:
                continue
            d = {}
            # 从i之后的子序列开始
            for y in nums[i+1:]:
                if y in d:
                    # 注意顺序, 先0-x-y, 后y
                    # #1 由于数组有序, -x-y先加入hashtable, 此时y是最大值, -x-y是较小的
                    # ## (x, y, -x-y) -> [-1, 1, 0]
                    # ## (x, -x-y, y) -> [-1, 0, 1]
                    res.add((x, -x-y, y))
                else:
                    # z = 0-x-y, 将推测值入哈希表
                    d[-x-y] = 0
        # set转化为list
        return list(res)

