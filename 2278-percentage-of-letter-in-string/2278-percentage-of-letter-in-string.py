class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0 
        for char in s:
            if char == letter:
                c = c+1
        sum1 = (floor((c/len(s))*100))
        return sum1
        