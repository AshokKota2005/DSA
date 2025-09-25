class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1 = list(str1)
        s2 = list(str2)
        d = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}
        s3 = []
        for i in range(0,len(s1)):
            s3.append(d[s1[i]])
        j = 0
        for i in range(0,len(s2)):
            flag = True
            while flag and j < len(s1):
                if s2[i] == s1[j] or s2[i] == s3[j]:
                    flag = False
                j = j+1
        if flag == False and i == len(s2)-1:
            return True
        else:
            return False

        
        