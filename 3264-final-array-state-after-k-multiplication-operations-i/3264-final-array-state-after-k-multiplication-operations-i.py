class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        i = 0
        while i < k:
            min1 = min(nums)
            index1 = nums.index(min1)
            min1 = multiplier * min1
            nums.pop(index1)
            nums.insert(index1,min1)
            i = i+1
        return nums
        