class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                val = nums[i]
                nums.pop(i) 
                nums.pop(i)
                nums.insert(i,val*2)
                nums.insert(i+1,0)
        c = 0
        while 0 in nums:
            nums.remove(0)
            c = c+1
        list1 = [0]*c
        nums.extend(list1)
        return nums
        

