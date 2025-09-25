class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ""
        for i in range(0,len(words)):
            res = res + words[i][0]  
        if res == s:
            return True
        else:
            return False
        