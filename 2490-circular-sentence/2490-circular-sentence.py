class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        list1 = sentence.split(" ")
        for i in range(0,len(list1)-1):
            if list1[i][-1] != list1[i+1][0]:
                return False
        return True
        