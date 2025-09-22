class Solution:
    def mySqrt(self, x: int) -> int:
        low ,high = 0,x
        res = 0
        while(low <= high):
            mid = (low+high)//2
            if((mid * mid) == x):
                return mid
            elif((mid * mid) < x):
                low = mid + 1
            else:
                high = mid - 1
                res = high
        return res 
        