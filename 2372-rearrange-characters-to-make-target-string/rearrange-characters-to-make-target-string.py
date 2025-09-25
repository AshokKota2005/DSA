class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d1 = {}
        for x in target:
            c = s.count(x)
            d1[x] = c
        print(d1)
        d2 = {}
        for char in target:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1
        print(d2)
        list3 = []
        for x in d2:
            list3.append(d1[x]//d2[x]) 
        return min(list3)


        