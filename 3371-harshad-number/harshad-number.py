class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        list1 = list(str(x))
        list1 = list(map(int,list1))
        sum1 = sum(list1)
        if x%sum1 == 0:
            return sum1
        else:
            return -1
        