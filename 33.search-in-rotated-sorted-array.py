#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 异常
        if not nums:
            return -1
        # init
        low = 0
        high = len(nums)-1

        # 边界不交叉
        while low <= high:
            # pivot选取 1/2
            mid = low + ((high-low) >> 1)
            # 满足返回
            if nums[mid] == target:
                return mid

            # 如果左侧升序(有=, 取中使用地板除, 会偏左, 导致low和mid重合)
            if nums[low] <= nums[mid]:
                # 如果target在升序区间内(注意由于上面已经过滤了nums[mid]=target)
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                # 否则
                else:
                    low = mid + 1
            # 左侧不升序, 右侧升序
            else:
                # target在右侧升序区间内
                if nums[mid] <= target <= nums[high]:
                    # 左侧右移
                    low = mid + 1
                else:
                    high = mid - 1
        # 不在数组内, 异常处理
        return -1

