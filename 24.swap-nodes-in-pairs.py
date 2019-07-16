#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # pre->a->b->c
        # pre->b->a->c
        dummy = pre = ListNode(-1)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            c = b.next
            pre.next, a.next, b.next = b, c, a
            pre = a
        return dummy.next




