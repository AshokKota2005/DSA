class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        length = len(searchWord)
        list1 = sentence.split(" ")
        for i in range(0,len(list1)):
            if searchWord in list1[i] and length <= len(list1[i]):
                check = list1[i][:length]
                if check == searchWord:
                    return i+1
        return -1

        