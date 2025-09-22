class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        for i in range(0,len(s)):
            if s[i].isalpha():
                res.append(s[i].upper())
            elif s[i].isdigit():
                res.append(s[i])
        res = res[::-1]
        result = ""
        m = k
        for i in range(0,len(res)):
            if len(result) == m:
                result = result + '-' 
                m = m + k + 1
            result = result + res[i]
        result = result[::-1]
        return result
        