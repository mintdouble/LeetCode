# 思路：通过表达式可以找到n(n),m(n)与n(n-1),m(n-1)的关系，也就是递推关系式
# 经过推导可以得出：n(n-1)=a(n-1)*n(n)+m(n),m(n-1)=n(n-1),也可以用递归来做
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        i = len(cont) - 1
        [n, m] = 1, 0
        while i >= 0:
            [n, m] = cont[i] * n + m, n
            i -= 1
        return [n, m]
