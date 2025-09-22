class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        list1 = []
        for char in s:
            strr = char[::-1]
            list1.append(strr)
        list1 = " ".join(list1)
        return list1
        