#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        思路:
        1.缺失的的数字, 一定位于[1...n+1]区间(n为数组长度)内
        2.数组值x(当x位于区间内)插入A[x-1](A[4]=5)
        3.第一个不满足此规律的位置i, i+1即为缺失的数字
        """
        length = len(nums)
        for i in range(length):
            # 值位于数组内且该值与下标不满足规律
            # 交换后新值如不满足规律, 继续直到满足或不在区间, 由于每次交换即固定一个结果, 所以虽然嵌套循环, 但是整体执行O(n)
            while 0 < nums[i] <= length and nums[nums[i]-1] != nums[i]:
                # 交换该值到正确位置
                # 同时新值插入当前位置, 新值如果位置不正确, 继续循环
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # 遍历, 第一个不满足规律的位置+1即为结果值(规律所得)
        for i in range(length):
            if nums[i] != i+1:
                return i + 1
        # 数组连续, 则返回n+1
        return length + 1
