class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        ans = 0
        num_zeroes = 0
        while r < len(nums): 
            if nums[r] == 0:
                num_zeroes += 1 
            if num_zeroes <= k:
                ans = max(ans,r-l+1)
            else:
                while num_zeroes > k:
                    if nums[l] == 0:
                        num_zeroes -= 1
                    l = l+1 
                ans = max(ans,r-l+1)
            r += 1
        return ans


