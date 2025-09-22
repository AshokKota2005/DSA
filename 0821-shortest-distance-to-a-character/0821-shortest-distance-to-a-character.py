class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ind = []
        for i in range(0,len(s)):
            if s[i] == c:
                ind.append(i)
        answer = []
        for i in range(0,len(s)):
            check = []
            for j in range(0,len(ind)):
                check.append(abs(i - ind[j])) 
            answer.append(min(check))
        return answer
         
        