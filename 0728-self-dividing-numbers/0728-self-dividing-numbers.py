class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list1 = []
        for i in range(left,right+1):
            if '0' not in str(i):
                temp = i
                while(temp > 0):
                    flag = 0
                    m = 0
                    rem = temp % 10
                    m = i % rem
                    if(m != 0):
                        flag = 1
                        break
                    temp = temp//10
                if (flag == 0):
                    list1.append(i)
        return list1

        