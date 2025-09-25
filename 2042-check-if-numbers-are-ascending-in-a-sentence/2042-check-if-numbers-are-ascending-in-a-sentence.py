class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        res = -1
        for i in range(0,len(s)):
            if s[i].isdigit():
                if int(s[i]) > res:
                    res = int(s[i])
                else:
                    return False
        return True
        