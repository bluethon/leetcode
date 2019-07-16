#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        二叉树深度优先遍历, 仅遍历根左子树部分节点(条件过滤)
        """
        # 结果集
        parens = []

        def dfs(p, left, right):
            """
            p: 已生成的括号序列
            left: 左括号剩余可用数
            right: 右括号剩余可用数
            """
            # 次数都用完, 添加答案, 返回
            if left == 0 and right == 0:
                parens.append(p)
                return
            # 左括号只要有就可以加入
            if left > 0:
                dfs(p + '(', left - 1, right)
            # 右括号待加入数量必须小于左括号, 防止出现')('
            if right > left:
                dfs(p + ')', left, right - 1)
        dfs('', n, n)
        return parens

    def generateParenthesis1(self, n: int) -> List[str]:
        # https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
        # parens=[], 在定义时初始化, 递归每次使用的都是同一个list, 可用id()验证
        def dfs(p, left, right, parens=[]):
            if left:
                dfs(p+'(', left-1, right)
            if right > left:
                dfs(p+')', left, right-1)
            if not right:
                # 数组合并, 注意最后有`,` 否则是单个字符加入list
                parens += p,
            return parens
        return dfs('', n, n)
