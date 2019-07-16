#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 小于0, 等价操作: 操作数取倒, 指数变正数
        if n < 0:
            n = -n
            x = 1 / x
        # 结果初始化, 乘法取1
        pow = 1
        # 指数循环, 直到为0, 操作完成
        while n:
            # 奇数, 单乘一次, 后续全是偶数情况(右移操作)
            if n & 1:
                pow *= x
            # 操作数自乘
            x *= x
            # 指数除2(右移一位)
            n >>= 1
        return pow

    def myPow1(self, x: float, n: int) -> float:
        # 如果为0
        if not n:
            return 1
        # 小于0为倒数
        if n < 0:
            return 1 / self.myPow(x, -n)
        # 大于0, 奇数
        if n % 2:
            return x * self.myPow(x, n-1)
        # 大于0, 偶数
        return self.myPow(x*x, n//2)
