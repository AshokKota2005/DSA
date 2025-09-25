class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []
        while len(nums) > 0:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            res.append(bob)
            res.append(alice)
        return res
            
        