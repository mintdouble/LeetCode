# 思路：这里我首先对房子的位置以及供暖器的位置进行了升序排序，然后比较两个供暖器之间的每个房子分别到两个供暖器之间的距离
# 取其中短的那个作为该房子的最短覆盖距离，最后对所有房子的最短覆盖距离求最大值即为所求
# 代码可再优化，不需要将每个房子的最短覆盖距离都保存起来
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters_point = 0
        houses_point = 0
        houses_min_radius = {}
        min_radius_max = 0
        houses_num = len(houses)
        heaters_num = len(heaters) - 1
        houses = sorted(houses)
        heaters = sorted(heaters)
        if heaters_num == 0:
            return abs(heaters[0]-houses[0]) if abs(heaters[0]-houses[0]) > abs(heaters[0]-houses[houses_num-1]) else abs(heaters[0]-houses[houses_num-1])
        while houses_point < houses_num:
            if heaters_point == 0:
                if houses[houses_point] <= heaters[heaters_point]:
                    houses_min_radius[houses[houses_point]] = heaters[heaters_point] - houses[houses_point]
                    if min_radius_max < houses_min_radius[houses[houses_point]]:
                        min_radius_max = houses_min_radius[houses[houses_point]]
                    houses_point += 1
                else:
                    heaters_point += 1
            elif heaters_point == heaters_num:
                if houses[houses_point] <= heaters[heaters_point]:
                    if heaters[heaters_point] - houses[houses_point] < houses[houses_point] - heaters[heaters_point-1]:
                        houses_min_radius[houses[houses_point]] = heaters[heaters_point] - houses[houses_point]
                    else:
                        houses_min_radius[houses[houses_point]] = houses[houses_point] - heaters[heaters_point-1]
                    if min_radius_max < houses_min_radius[houses[houses_point]]:
                        min_radius_max = houses_min_radius[houses[houses_point]]
                    houses_point += 1
                else:
                    houses_min_radius[houses[houses_point]] = houses[houses_point] - heaters[heaters_point]
                    if min_radius_max < houses_min_radius[houses[houses_point]]:
                        min_radius_max = houses_min_radius[houses[houses_point]]
                    houses_point += 1
            else:
                if houses[houses_point] <= heaters[heaters_point]:
                    if heaters[heaters_point] - houses[houses_point] < houses[houses_point] - heaters[heaters_point-1]:
                        houses_min_radius[houses[houses_point]] = heaters[heaters_point] - houses[houses_point]
                    else:
                        houses_min_radius[houses[houses_point]] = houses[houses_point] - heaters[heaters_point-1]
                    if min_radius_max < houses_min_radius[houses[houses_point]]:
                        min_radius_max = houses_min_radius[houses[houses_point]]
                    houses_point += 1
                else:
                    heaters_point += 1           
        return min_radius_max
