class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            total = 0
            while(n > 0):
                rem = n%10
                total = total + rem * rem
                n = n//10
            n = total
        return n==1
        