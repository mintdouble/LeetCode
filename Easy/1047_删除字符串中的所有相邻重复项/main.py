# 思路：用栈来求解，将元素与栈中的最后一个元素进行对比，如果相同，则将栈中最后一个元素弹出，不相同则将元素存入栈中
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ['']
        for i in S:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
            
