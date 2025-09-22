class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum1 = 0
        pre_value = 0
        for char in reversed(s):
            if d[char] < pre_value:
                sum1 = sum1 - d[char]
            else:
                sum1 = sum1 + d[char]
                pre_value = d[char]
        return sum1

             
        