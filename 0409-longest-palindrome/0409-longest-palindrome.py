class Solution:
    def longestPalindrome(self, s: str) -> int:
        length1 = 0
        for char in s:
            length1 += 1
        if(length1 == 0):
            return 0
        elif(length1 == 1):
            return  1
        else:
            char_count = {}
            for char in s:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            length = 0
            odd_found = False
            for count in char_count.values():
                length += (count // 2) * 2  
                if count % 2 == 1:  
                    odd_found = True
            if odd_found:
                length += 1
            return length
            