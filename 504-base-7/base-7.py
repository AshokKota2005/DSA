class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        num = str(num)
        flag = True
        if num[0] == '-':
            flag = False
            num = num[1:]
        num = int(num) 
        res = ""
        while num != 0:
            rem = num%7 
            res = res + str(rem)
            num = num//7 
        if flag == False:
            res = res + '-'
        res = res[::-1]
        return res
        