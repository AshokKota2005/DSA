class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        vowels = ['a','e','i','o','u']
        consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        vowel = 0
        digit = 0
        consonant = 0
        for char in word:
            if char in vowels:
                vowel = vowel + 1
            elif char in consonants:
                consonant=consonant+1
            elif char >= '0' and char <= '9':
                digit = digit + 1
            else:
                return False
        if vowel > 0 and consonant > 0 and len(word) >= 3:
            return True
        else:
            return False 
        
        
        