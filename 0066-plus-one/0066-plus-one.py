class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''.join(map(str,digits))
        nums = int(nums) + 1
        nums = list(map(int,str(nums)))    
        return nums
        