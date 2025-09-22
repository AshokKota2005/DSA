class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if(num%2 != 0):
            return False 
        temp = 0
        for i in range(1,(num//2)+1):
            if(num%i == 0):
                temp = temp + i
        if(temp == num):
            return True
        else:
            return False