# 思路：偷懒使用replace函数
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
