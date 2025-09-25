class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        c = -1
        flag = 'low'
        for i in range(0,k+1):
            if flag == 'low':
                c += 1
            elif flag == 'high':
                c -= 1
            if c == 0:
                flag = 'low'
            elif c == n-1:
                flag = 'high'
        return c
        
        