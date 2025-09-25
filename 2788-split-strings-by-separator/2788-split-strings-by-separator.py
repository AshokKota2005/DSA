class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in range(0,len(words)):
            if separator in words[i]:
                list1 = words[i].split(separator)
                res.extend(list1)
            else:
                res.append(words[i])
        res = ' '.join(res).split()
        return res


        