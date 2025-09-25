class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = '0'
        temp = number
        for i in range(0,len(temp)):
            if temp[i] == digit:
                temp = temp[:i] + temp[i+1:]
                print(temp)
                if temp > res :
                    res = temp
            temp = number
        return res 
        