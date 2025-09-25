class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(0,n):
            for j in range(0,n-i-1):
                swap = False
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    swap = True
                if swap == True:
                    names[j],names[j+1] = names[j+1],names[j]
        return names
                

        