# 思路：要么顺时针距离最小，要么逆时针距离最小，只要计算一个方向的距离，再用所有距离之和减去这个距离就是另一个方向的距离，返回小的距离
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_d = sum(distance)
        if start < destination:
            d = sum(distance[start:destination])
        else:
            d = sum(distance[destination:start])
        return d if d < sum_d - d else sum_d - d
