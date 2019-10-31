# 思路：利用对撞指针，判断一个从头往后遍历，一个从头往前遍历，如果指针指向的字符都是字母，则交换字母，如果指针指向的不是字母则指针向前移动或者向后移动
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        charset = set(['a','b','c','d','e','f','g','h',
                      'i','j','k','l','m','n','o','p',
                      'q','r','s','t','u','v','w','x',
                       'y','z','A','B','C','D','E','F',
                      'G','H','I','J','K','L','M','N',
                      'O','P','Q','R','S','T','U','V',
                      'W','X','Y','Z'])
        i,j = 0,len(S)-1
        S = list(S)
        while i < j:
            if S[i] not in charset:
                i += 1
                continue
            if S[j] not in charset:
                j -= 1
                continue
            if S[i] in charset and S[j] in charset:
                tmp = S[i]
                S[i] = S[j]
                S[j] = tmp
                i += 1
                j -= 1
        return ''.join(S)
