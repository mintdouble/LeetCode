# 思路：统计每个字母出现的次数，如果为偶数，则该字母一定能构成回文串，如果为奇数，则至少有一个该字母不能构成回文串
# 统计出现次数为奇数的字母个数，如果这样的字母个数大于等于1，则回文串的总长度为字符串长度减去出现奇次数字母的个数加1
# 如果没有出现过奇次数的字母，则所有字母都能构成回文串
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        count = 0
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in dic.keys():
            if dic[j] % 2 != 0:
                count += 1
        return len(s)-count+1 if count > 0 else len(s)
