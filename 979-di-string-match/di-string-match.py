class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        list1  =[]
        for i in range(0,len(s)+1):
            list1.append(i)
        res = []
        for i in range(0,len(s)):
            if s[i] == 'I':
                res.append(list1[0])
                list1.pop(0)
            else:
                res.append(list1[-1])
                list1.pop()
        res = res + list1
        return res
        

        