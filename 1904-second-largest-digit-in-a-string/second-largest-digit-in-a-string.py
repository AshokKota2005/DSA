class Solution:
    def secondHighest(self, s: str) -> int:
        list1 = []
        for i in range(0,len(s)):
            if s[i].isdigit():
                list1.append(s[i])
        list1 = list(set(list1)) 
        if len(list1) > 1:
            list1.sort(reverse = True)
            return int(list1[1])
        else:
            return -1