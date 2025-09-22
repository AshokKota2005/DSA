class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        soar = dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
        res = ""
        for x in soar:
            res = res + x * soar[x]
        return res

        