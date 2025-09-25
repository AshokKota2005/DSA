class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = len(s) + k
        diff = k%len(s)
        diff = len(s) - diff
        str1 = s[:len(s) - diff]
        str2 = s[len(s) - diff:]
        res = str2 + str1
        print(str1)
        print(str2) 
        return res       