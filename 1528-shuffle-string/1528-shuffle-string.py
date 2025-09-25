class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        s = list(s)
        for i in range(0,n):
            for j in range(0,n-i-1):
                swap = False
                if indices[j] > indices[j+1]:
                    swap = True
                    indices[j],indices[j+1] = indices[j+1],indices[j]
                if swap == True:
                    s[j],s[j+1] = s[j+1],s[j]
        s = "".join(s)
        return s
        