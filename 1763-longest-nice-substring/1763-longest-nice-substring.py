class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        list1 = []
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                k = s[i:j]
                if len(k) > 1:
                    list1.append(k)
        res = ""
        for char in list1:
            flag = True
            for j in range(0,len(char)):
                check = ord(char[j]) 
                if check >= 65 and check <= 90:
                    check = chr(check+32)
                    if check not in char:
                        flag = False
                        break
                else:
                    check = chr(check - 32)
                    if check not in char:
                        flag = False
                        break
            if flag == True and len(char) > len(res):
                res = char
        return res
          
        