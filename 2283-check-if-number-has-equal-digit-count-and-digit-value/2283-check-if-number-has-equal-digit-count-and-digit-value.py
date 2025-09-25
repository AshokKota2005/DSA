class Solution:
    def digitCount(self, num: str) -> bool:
        nums = list(num)
        for i in range(0,len(num)):
            if(int(num[i]) == nums.count(str(i))):
                pass
            else:
                return False
        return True