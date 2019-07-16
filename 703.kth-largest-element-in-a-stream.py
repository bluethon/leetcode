#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = nums
        self.k = k
        heapq.heapify(self.hq)
        while len(self.hq) > k:
            heapq.heappop(self.hq)

    def add(self, val: int) -> int:
        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
        if len(self.hq) < self.k:
            heapq.heappush(self.hq, val)
        else:
            heapq.heappushpop(self.hq, val)
        return self.hq[0]
