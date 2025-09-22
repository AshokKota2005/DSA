class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        for i in range(0,len(words)):
            if words[i][0] in ('a','e','i','o','u','A','E','I','O','U'):
                words[i] = words[i] + 'ma' + 'a' * (i+1)
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma' + 'a' * (i+1) 
        res = " ".join(words)
        return res
        