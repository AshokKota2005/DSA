class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = list(map(str,nums))
        for i in range(0,len(nums)):
            k = nums[i][::-1]
            while k[0] == '0':
                k = k[1:]
            nums.append(k)
        nums = set(nums)
        return len(nums)      