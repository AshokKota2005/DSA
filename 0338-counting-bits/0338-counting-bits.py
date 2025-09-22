class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = []
        for i in range(0,n+1):
            k = bin(i)[2:]
            m = k.count('1')
            list1.append(m)
        return list1
        