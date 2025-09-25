class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        list1 = []
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                list1.append(s[i:j])
        count = 0
        for i in range(0,len(list1)):
            if list1[i].count('0') <= k or list1[i].count('1') <= k:
                count += 1
        return count
        
        