class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        i,j = 0,len(s)-1
        while i<j:
            while i<j and s[i] not in vowels:
                i = i+1
            while i<j and s[j] not in vowels:
                j = j-1
            s[i],s[j] = s[j],s[i]
            i = i+1
            j = j-1

        s = "".join(s)
        return s
        