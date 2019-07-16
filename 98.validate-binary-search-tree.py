#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 参考优化v2, 递归: 当前节点是左子树的最大值, 右子树的最小值
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, min, max) -> bool:
            if not node:
                return True
            return min < node.val < max and helper(node.left, min, node.val) and helper(node.right, node.val, max)
        return helper(root, float('-inf'), float('inf'))

    # 中序遍历优化v4(O(1) space), 中序即为升序, 所以prev节点值小于当前节点
    def isValidBST4(self, root: TreeNode) -> bool:
        self.prev = float('-inf')
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return True
        if not self.inorder(node.left):
            return False
        if node.val <= self.prev:
            return False
        self.prev = node.val
        if not self.inorder(node.right):
            return False
        return True

    # 中序遍历v3
    def isValidBST3(self, root: TreeNode) -> bool:
        def inorderT(node, order):
            if not node:
                return
            inorderT(node.left, order)
            order.append(node.val)
            inorderT(node.right, order)
        order = []
        inorderT(root, order)
        # 循环到n-1, 否则越界
        for i in range(len(order)-1):
            if order[i] >= order[i+1]:
                return False
        # 注意缩进, 循环完成后返回True
        return True

    # 自己版本v1
    def isValidBST1(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, min: int, max: int) -> bool:
            if not node:
                return True
            # min和max可能为0, 不能写成if min, 必须是is not None
            if min is not None and node.val <= min:
                return False
            if max is not None and node.val >= max:
                return False
            return helper(node.left, min, node.val) and helper(node.right, node.val, max)

        return helper(root, None, None)
