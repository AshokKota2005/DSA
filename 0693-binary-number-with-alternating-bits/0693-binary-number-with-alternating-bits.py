class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = ""
        while n > 0:
            print('n=',n)
            rem = n%2
            print("rem=",rem)
            if len(res) > 0:
                if str(rem) == res[-1]:
                    print("A")
                    return False
            res += str(rem)
            print(res)
            n = n//2
            print("--------")
        return True
        
        