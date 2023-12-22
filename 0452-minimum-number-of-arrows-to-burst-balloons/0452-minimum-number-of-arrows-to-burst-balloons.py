class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) == 1:
            return 1
        
        points.sort(key=lambda x: x[0])
        count = 1

        start = points[0][0]
        end = points[0][1]

        for i in range(1, len(points)):
            
            if points[i][0] > end:
                count += 1
                start = points[i][0]
                end = points[i][1]
            elif points[i][1] <= end:
                start = points[i][0]
                end = points[i][1]
            elif points[i][0] <= end:
                start = points[i][0]

        return count



        