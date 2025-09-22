class Solution:
    def addDigits(self, num: int) -> int:
        if(0 <= num <= 2147483647):
            if(num >= 0 and num <= 9):
                return num
            length1 = 0
            temp = num
            while(num != 0):
                length1 += 1
                num = num // 10
            num = temp
            while(length1!=1):
                sum1 = 0
                rem = 0
                while(num != 0):
                    rem = num%10
                    sum1 = sum1 + rem
                    num = num//10
                num = sum1
                length1 = 0
                temp = num
                while(num != 0):
                    length1 += 1
                    num = num//10
                num = temp
            return sum1 