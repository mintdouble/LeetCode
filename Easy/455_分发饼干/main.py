# 思路：分别对两个列表进行排序，从最小值开始比较，如果胃口大于饼干，则饼干后移一个
# 如果胃口小于等于饼干，则计数加一，饼干后移一位，胃口也后移移位，直到其中一个移到结尾
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        g_i = 0
        s_i = 0
        count = 0
        while g_i < len(g) and s_i < len(s):
            if g[g_i] > s[s_i]:
                s_i += 1
            else:
                count += 1
                g_i += 1
                s_i += 1
        return count
