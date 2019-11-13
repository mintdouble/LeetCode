# 思路：利用二进制位的思想，集合子集的个数为2**len(集合)，因此从0到2**len()-1的二进制数，当位为1则把集合中该位置上的数存入子集中
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        for i in range(2**len(nums)):
            bin_i = bin(i)
            tmp = []
            for j in range(-1,-len(bin_i)+1,-1):
                if bin_i[j] == '1':
                    tmp.append(nums[j])
            sub.append(tmp)
        return sub
