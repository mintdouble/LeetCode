# 思路：用栈来存字符串，当匹配到有效的括号时，弹出栈顶元素，否则将元素弹入栈中
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = ['']
        for i in S:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        return len(stack) - 1
