class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        list1 = []
        for x in candyType:
            if len(list1) != len(candyType)//2:
                if x not in list1:
                    list1.append(x)
        return len(list1)


        