#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        # 注意检测slow和fast
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 使用is, 不用==
            if slow is fast:
                return True
        return False

