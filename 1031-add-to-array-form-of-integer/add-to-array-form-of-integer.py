class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = list(map(str,num))
        s = "".join(num)
        nums2 = 0
        for char in s:
            digit = ord(char) - ord('0')
            nums2 = nums2 * 10 + digit
        res1 = nums2+k
        res2 = []
        while res1 > 0:
            rem = res1 % 10 
            res2.append(chr(ord('0') + rem)) 
            res1 //= 10 
         
        res = list(map(int,res2))
        return res[::-1]