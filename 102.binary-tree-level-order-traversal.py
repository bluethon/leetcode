#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        pass
        # 边界
        if not root:
            return []
        # 结果, 当前层初始化
        res, cur_level = [], [root]
        while cur_level:
            tmp, next_level = [], []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur_level = next_level
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        # 递归
        def dfs(node, level, res):
            # 边界, 空
            if not node:
                return
            # 层级等于数据长度, 即新一层开始, 初始化一个空数组, 方便后续append
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)
        # 初始化
        res = []
        # 从0层开始调用
        dfs(root, 0, res)
        # 返回数组
        return res
