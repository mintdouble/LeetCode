# 思路：根据斜率来判断点是否在线上，如果只有两个点，则一定在直线上，当大于两个点时，根据前两个点可以算出直线的斜率
# 但是这里不要把斜率的结果给算出来，因为相除的话得到的是浮点数，所以将斜率以分数的形式保存其分子和分母
# 然后将斜率的除运算转换成对应的乘积运算，即d_y2/d_x2=d_y1/d_x1表示成d_y2*d_x1=d_y1*d_x2的形式，保证其结果为整形才能进行比较
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            de_x = coordinates[1][0] - coordinates[0][0]
            de_y = coordinates[1][1] - coordinates[0][1]
            for i in range(2, len(coordinates)):
                if (coordinates[i][0] - coordinates[0][0])*de_y != (coordinates[i][1] - coordinates[0][1])*de_x:
                    return False
            return True
