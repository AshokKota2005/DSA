class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strr = ""
        length = len(s)
        for i in range(0,length):
            if (s[i].isalnum()):
                strr = strr + s[i]
        if (strr == strr[::-1]):
            return True
        else:
            return False        