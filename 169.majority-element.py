#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        length = len(nums) / 2
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > length:
                return n

    def majorityElement1(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
