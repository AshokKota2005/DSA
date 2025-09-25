class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        text = text.split(" ")
        for i in range(0,len(text)):
            flag = True
            for j in range(0,len(brokenLetters)):
                if brokenLetters[j] in text[i]:
                    flag = False
                    break
            if flag == True:
                count += 1
        return count
        