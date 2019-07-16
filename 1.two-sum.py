#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(nums):
            if x in dic:
                return [dic[x], i]
            else:
                dic[target - x] = i

