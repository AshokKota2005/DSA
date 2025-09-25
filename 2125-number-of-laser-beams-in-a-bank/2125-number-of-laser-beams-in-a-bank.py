class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        list1 = []
        for i in range(0,len(bank)):
            if '1' in bank[i]:
                list1.append(bank[i].count('1'))
        res = 0
        for i in range(0,len(list1)-1):
            res = res + list1[i] * list1[i+1]
        return res
         
        