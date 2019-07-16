#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 初始化
        prev, cur = None, head
        while cur:
            # 等式右边一次性计算出真实值
            # 左边依次赋值, 所以要先给prev, 在prev.next
            prev, prev.next, cur = cur, prev, cur.next
        return prev

