# 思路：从低位开始相加，设置进位标志
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        num_sum = ''
        if len(num1) < len(num2):
            tmp = num1
            num1 = num2
            num2 = tmp
        i = -1
        while abs(i) <= len(num1):
            if abs(i) <= len(num2):
                add_num = int(num1[i]) + int(num2[i]) + carry
                if add_num > 9:
                    carry = 1
                    num_sum = str(add_num%10) + num_sum
                else:
                    carry = 0
                    num_sum = str(add_num) + num_sum
            else:
                if carry == 0:
                    num_sum = num1[0:len(num1)-abs(i)+1] + num_sum
                    break
                else:
                    add_num = int(num1[i]) + carry
                    if add_num > 9:
                        carry = 1
                        num_sum = '0' + num_sum
                    else:
                        carry = 0
                        num_sum = str(add_num) + num_sum
            i -= 1
        if carry == 1:
            num_sum = '1' + num_sum
        return num_sum
