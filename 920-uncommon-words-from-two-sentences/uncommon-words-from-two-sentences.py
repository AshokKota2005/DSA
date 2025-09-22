class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1 = []
        res = s1 +" "+ s2
        res = list(res.split())
        for char in res:
            c = 0
            for key in res:
                if(char == key):
                    c = c+1
            if (c == 1):
                list1.append(char)
        return list1
            