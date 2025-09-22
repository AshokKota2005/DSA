from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        list1 = []
        for i in digits:
            list1.append(d[i])
        list2 = list(product(*list1))
        list3 = []
        for i in range(0,len(list2)):
            list2[i] = "".join(list2[i])
        return list2


        