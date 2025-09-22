class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].isalpha():
                if s[j].isalpha():
                    s[i],s[j] = s[j],s[i]
                    i = i+1
                    j = j-1
                else:
                    j = j-1
            else:
                i = i+1
        s = "".join(s)
        return s


        