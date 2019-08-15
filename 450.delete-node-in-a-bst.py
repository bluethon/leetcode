#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 退出条件, 节点没有(包含根节点没有和找不到)
        if not root:
            return

        # BST性质, 查找在哪边, 递归
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # 找到了
        else:
            # 情况1, 右子树不存在, 直接返回左子树
            if not root.right:
                return root.left
            # 情况2, 左子树不存在, 直接返回右子树
            elif not root.left:
                return root.right
            # 情况3, 最复杂, 都存在, 找左子树最大或右子树最小
            else:
                # 找右子树最小节点
                min = root.right
                # 最小节点必定是左叶子(性质)
                while min.left:
                    min = min.left
                # 交换root和min的值, 这样不用移动root
                root.val = min.val
                # 递归, 此时问题变为, 右子树中移除刚才的min节点
                root.right = self.deleteNode(root.right, min.val)
        # 操作完成, 返回根节点
        return root

