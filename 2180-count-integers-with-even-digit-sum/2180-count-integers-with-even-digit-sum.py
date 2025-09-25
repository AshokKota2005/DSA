class Solution:
    def countEven(self, num: int) -> int:
        c = 0 
        for i in range(1,num+1):
            sum1 = 0
            while(i > 0):
                rem = i%10
                sum1 = sum1+rem
                i = i//10
            if(sum1%2 == 0):
                c += 1
        return c