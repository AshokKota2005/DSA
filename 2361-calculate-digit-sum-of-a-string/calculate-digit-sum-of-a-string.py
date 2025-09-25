class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s) > k):
            result = ""
            for i in range(0,len(s),+k):
                res = s[i:k+i]
                res = int(res)
                sum1 = 0
                while(res > 0):
                    rem = res%10
                    sum1 = sum1+rem
                    res = res//10
                result = result + str(sum1)
            s = result
        return s 
        