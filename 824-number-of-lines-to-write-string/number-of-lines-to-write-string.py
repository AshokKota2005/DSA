class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count = 1
        sum1 = 0
        for i in range(0,len(s)):
            val = ord(s[i]) - 97
            if sum1+widths[val] > 100:
                sum1 = widths[val]
                count += 1
            else:
                sum1 += widths[val]
            
        return [count,sum1] 
                

        