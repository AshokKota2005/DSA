class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        height = sorted(heights)
        for i in range(0,len(heights)):
            if height[i] != heights[i]:
                count  += 1
        return count
            
        