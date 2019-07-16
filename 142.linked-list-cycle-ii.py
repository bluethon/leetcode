#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycleV1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        hash_map = set()
        while cur:
            if cur in hash_map:
                return cur
            else:
                hash_map.add(cur)
            cur = cur.next
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # H: 起点到环
        # D: 环到相遇点
        # L: 环长
        # 快比慢多一倍
        # 2(H + D) = H + D + nL
        # H = nL - D
        # 即起点到环 = 绕N圈-D(即走N-1圈+从相遇点走到环开始, 这里相遇)
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
