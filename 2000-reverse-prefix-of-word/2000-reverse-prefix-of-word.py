class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            prefix = ""
            index1 = word.index(ch)
            prefix = word[0:index1+1][::-1] + word[index1+1:] 
            return prefix

        