class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if(num1 == '0' and num2 == '0'):
            return "0"
        nums1 = 0
        for char in num1:
            digit = ord(char) - ord('0') 
            nums1 = nums1 * 10 + digit
        nums2 = 0
        for char in num2:
            digit = ord(char) - ord('0') 
            nums2 = nums2 * 10 + digit 
        nums3 = nums1 + nums2
        digits = []
        while nums3 > 0:
            digit = nums3 % 10
            digits.append(chr(ord('0') + digit))
            nums3 //= 10
        result = ''.join(digits[::-1])
        return result
        