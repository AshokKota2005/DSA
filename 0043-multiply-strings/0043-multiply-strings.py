class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res1 = 0
        for char in num1:
            res1 = res1 * 10 + (ord(char) - ord('0'))
        res2 = 0
        for char in num2:
            res2 = res2 * 10 + (ord(char) - ord('0'))
        res3 = res1 * res2
        result = []
        while res3 > 0:
            result.append(chr(ord('0') + res3 % 10))
            res3 //= 10
        result = result[::-1]
        result = "".join(result)
        return result
    
                