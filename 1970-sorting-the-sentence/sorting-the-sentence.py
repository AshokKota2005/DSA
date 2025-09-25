class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        for i in range(0,len(s)):
            s[i] = s[i][::-1]
        s.sort()
        for i in range(0,len(s)):
            s[i] = s[i][1:]
            s[i] = s[i][::-1]
        s = " ".join(s)
        return s