class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(0,len(s)):
            for  j in range(0,len(s)):
                if s[i] == s[j] and i != j:
                    res = abs(i - j) - 1
                    check = ord(s[i]) - 97
                    if distance[check] != res:
                        return False
        return True
            
        