class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True
        s = list(magazine)
        for char in ransomNote:
            if char in s:
                s.remove(char)
            else:
                return False
        return True
        