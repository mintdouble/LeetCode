# 思路：统计0-59的二进制表示中1的个数，有几个1代表亮几个灯，hour数组中保存的是0-11中亮数组下标个灯能表示的数字
# minute数组中保存的是0-59中亮数组下标个灯能表示的数字
# 分析num能由几个hour中的灯和几个minute中的灯组合而成
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num > 8:
            return []
        hour = [['0'],[],[],[]]
        minute = [['00'],[],[],[],[],[]]
        result = []
        for i in range(1,60):
            j = i
            count_1 = 0
            while j > 0:
                if j % 2 != 0:
                    count_1 += 1
                j >>= 1 
            if i < 12:
                hour[count_1].append(str(i))
            if i < 10:
                minute[count_1].append('0'+str(i))
            else:
                minute[count_1].append(str(i))
        for i in range(min(3,num)+1):
            if num - i < 6:
                for j in hour[i]:
                    for k in minute[num-i]:
                        result.append(j+':'+k)
        return result
