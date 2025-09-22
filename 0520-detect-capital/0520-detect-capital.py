class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.istitle() or word.islower() or word.isupper()):
            return True
        return False

        