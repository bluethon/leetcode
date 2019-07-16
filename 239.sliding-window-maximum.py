#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window = deque()
        res = []
        for i, x in enumerate(nums):
            # 如果新入值x大于它左侧的窗口内任意值,
            # 则等效只有x最终生效, 丢弃窗口内其他值的序号
            while window and nums[window[-1]] < x:
                window.pop()
            # 新值序号必定加入窗口
            window.append(i)

            # 如果窗口内最大值=窗口外左侧序号(窗口已经移过[0]), 剔除
            # 写在append之前会导致第一次window[0]没有值
            if window[0] == i-k:
                window.popleft()
            # 窗口大小足够后开始塞值
            if i >= k -1:
                res.append(nums[window[0]])
        return res
