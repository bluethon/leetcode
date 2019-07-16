#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['#']
        m = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in m:
                if m[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return len(stack) == 1


