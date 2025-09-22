class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left,right = 0,len(height)-1
        while left < right:
            min1 = min(height[left],height[right])
            area = (right - left) * min1
            res = max(area,res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


        