class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for char in words:
            flag = 0
            for i in char:
                if i not in allowed:
                    flag = 1
                    break
            if flag == 0:
                c = c+1
        return c
                
        