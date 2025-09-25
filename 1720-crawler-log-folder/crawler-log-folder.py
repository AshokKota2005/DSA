class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for char in logs:
            if '../' in char:
                if c == 0:
                    c = c
                else:
                    c = c-1
            elif './' in char:
                c = c
            elif '/' in char:
                c = c+1
        return c

        