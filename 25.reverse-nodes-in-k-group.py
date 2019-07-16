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
        # node存在, 可以next, 且数量足够
        while node and count < k:
            node = node.next
            count += 1
        # 不足则不反转, 直接返回head
        if count < k:
            return head
        # 递归的子链表的头, 已反转部分的链表头
        new_head, pre = self.reverse(head, k)
        # 当前head为反转前的表头(即反转后的tail)
        # .next存储子问题的的表头
        head.next = self.reverseKGroup(new_head, k)
        # 返回已反转后的链表头
        return pre

    def reverse(self, head: ListNode, k: int):
        pre = None
        cur = head
        while k > 0:
            pre, pre.next, cur = cur, pre, cur.next
            k -= 1
        # 返回下个group的head, 反转部分链表的head
        return cur, pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # dummy, 虚拟头指针
        # pre_tail, 上个Group尾指针
        dummy = pre_tail = ListNode(-1)
        # l, Group最左节点
        # r, 下个Group最左节点
        # dummy.next, 真头节点
        dummy.next = l = r = head
        while True:
            count = 0
            # 是否还有k个节点
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                # 类似反转链表, 特殊pre=r
                pre, cur = r, l
                for _ in range(k):
                    pre, pre.next, cur = cur, pre, cur.next
                # 调整各指针位置
                # 上个group尾节点的后继=反转进行的结尾(由于反转了, 所有是头), 连接上了pre Group和 cur Group
                # pre Group后移为l(反转后为尾节点)
                # l移到r, 下个group开始位置
                pre_tail.next, pre_tail, l = pre, l, r
            else:
                # 节点不足, 返回真头结点
                return dummy.next

