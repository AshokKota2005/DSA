class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = []
        for i in range(0,len(points)-1):
            res.append(abs(points[i][0] - points[i+1][0]))
        return max(res) 

        