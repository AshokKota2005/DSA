class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] in (10,20):
            return False
        a,b,c = 0,0,0
        for char in bills:
            if char == 5:
                a = a+1
            elif char == 10:
                if a > 0:
                    b = b+1
                    a =a-1
                else:
                    return False
            elif char == 20:
                c = c+1
                if a>0 and b>0:
                    b = b-1
                    a = a-1 
                elif a > 2:
                    a = a-3
                else:
                    return False
        return True