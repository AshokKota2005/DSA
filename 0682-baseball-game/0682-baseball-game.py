class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1 = []
        for char in operations:
            if char not in ('C','D','+'):
                list1.append(int(char))
            elif(char == 'C'):
                if (len(list1) > 1):
                    list1 = list1[::-1]
                    list1 = list1[1:]
                    list1 = list1[::-1]
                else:
                    list1 = []
            elif(char == 'D'):
                list1 = list1[::-1]
                rem = list1[0]
                list1 = list1[::-1]  
                list1.append(rem*2)
            elif(char == '+'):
                list1 = list1[::-1]
                a = list1[0]
                b = list1[1]
                list1 = list1[::-1]
                rem = a+b
                list1.append(rem)
        sum1 = 0
        for char in list1:
            sum1 = sum1 + char
        return sum1


        