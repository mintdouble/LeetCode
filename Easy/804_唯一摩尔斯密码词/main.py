# 思路：建立摩尔斯密码转换字典，根据字母和摩尔斯密码进行转换，最后将转化后的摩尔斯密码存入集合，返回集合的长度
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {'a':'.-','b':'-...','c':'-.-.','d':'-..',
              'e':'.','f':'..-.','g':'--.','h':'....',
              'i':'..','j':'.---','k':'-.-','l':'.-..',
              'm':'--','n':'-.','o':'---','p':'.--.',
              'q':'--.-','r':'.-.','s':'...','t':'-',
              'u':'..-','v':'...-','w':'.--','x':'-..-',
              'y':'-.--','z':'--..'}
        count = 0
        for i in words:
            tmp = ''
            for j in i:
                tmp += dic[j]
            words[count] = tmp
            count += 1
        return len(set(words))
