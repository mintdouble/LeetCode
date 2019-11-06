# 思路：遍历比较大小，优化可用二分查找
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]
