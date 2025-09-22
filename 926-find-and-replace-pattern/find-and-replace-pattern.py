class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for i in range(0,len(words)):
            print(i)
            s1 = words[i]
            s2 = pattern
            s3 = set(list(s1))
            s4 = set(list(s2))
            if len(s3) == len(s4):
                d = {}
                flag = True
                for j in range(0,len(s1)):
                    if s1[j] not in d:
                        d[s1[j]] = s2[j]
                    else:
                        temp = d[s1[j]]
                        if temp != s2[j]:
                            flag = False
                            break
                if flag == True:
                    res.append(s1)
        return res

        