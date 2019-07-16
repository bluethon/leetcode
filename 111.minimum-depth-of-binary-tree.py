#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 从下到上逐层累加
        # 边界
        if not root:
            return 0
        # 层级
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        # 如果是单支, 左或右子树一边不存在, 则为0, 加不加不影响结果, 但是可以简化成一行
        if not root.left or not root.right:
            return l+r+1
        else:
            # 如果两边都有或为叶子, 则最小值的一边+1(当前层)
            return min(l, r) + 1
