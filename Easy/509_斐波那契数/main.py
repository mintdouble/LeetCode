# 思路：只更新fn-1和fn-2即可
class Solution:
    def fib(self, N: int) -> int:
        f = [0,1]
        for i in range(2,N+1):
            f[i&1] = f[0] + f[1]
        return f[N&1]
