# 思路：利用栈，遇到左括号就入栈，遇到右括号就出栈，栈空则找到了一个原语，将首尾下标保留
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ''
        i,j = 0,0
        while j < len(S):
            if S[j] == '(':
                stack.append(S[j])
            else:
                stack.pop()
            if len(stack) == 0:
                result += S[i+1:j]
                i = j + 1
            j += 1
        return result
