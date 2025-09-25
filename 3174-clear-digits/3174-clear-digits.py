class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i-1
                while j >= 0:
                    if s[j].isalpha():
                        s.pop(j)
                        s.pop(j)
                        i = i-1
                        break
                    j = j-1
            else:
                i += 1
        res = "".join(s)
        return res



        