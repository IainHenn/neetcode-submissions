import math
class Solution:
    # Have a priority list of the indexes to the pairs in order of their distance?
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_tuple = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0]**2) + (points[i][1]**2))
            point_tuple.append((points[i], dist))

        print(point_tuple)
        
        achieved = 0
        li_to_return = []
        while achieved != k:
            i = 0
            min = 1001
            min_idx = -1
            while i < len(point_tuple):
                if point_tuple[i][1] < min:
                    min = point_tuple[i][1]
                    min_idx = i
                i += 1

            li_to_return.append(point_tuple[min_idx][0])
            point_tuple.pop(min_idx)
            achieved += 1
        
        return li_to_return