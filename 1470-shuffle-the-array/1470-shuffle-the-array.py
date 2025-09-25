class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)
        res = []
        for i in range(0,length//2):
            res.append(nums[i])
            res.append(nums[length//2+i])
        return res