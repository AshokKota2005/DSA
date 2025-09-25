class Solution:
    def convertDateToBinary(self, date: str) -> str:
        list1 = list(date.split('-'))
        list2 = []
        for i in list1:
            binaryy = bin(int(i))
            list2.append(binaryy[2:])
        list2 = "-".join(list2)
        return str(list2)
        