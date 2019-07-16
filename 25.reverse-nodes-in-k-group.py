#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup_re(self, head: ListNode, k: int) -> ListNode:
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        new_head, pre = self.reverse(head, k)
        head.next = self.reverseKGroup(new_head, k)
        return pre

    def reverse(self, head: ListNode, k: int):
        pre = None
        cur = head
        while k > 0:
            pre, pre.next, cur = cur, pre, cur.next
            k -= 1
        return cur, pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    pre, pre.next, cur = cur, pre, cur.next
                # jump.next时jump代指dummp(上个节点)
                jump.next, jump, l = pre, l, r
            else:
                # r为None, 剩余不足, 退出算法
                return dummy.next

