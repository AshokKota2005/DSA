class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        flag = 1
        while(flag == 1):
            if(original in nums):
                original = 2 * original
            else:
                flag = 0
        return original        
        