class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        list1 = []
        k = 0
        for words in words1:
            a = 0
            for word in words1:
                if words == word:
                    a = a+1
            b = 0
            for word in words2:
                if words == word:
                    b = b+1
            if(a==1 and b==1):
                k = k+1
        return k
            
        