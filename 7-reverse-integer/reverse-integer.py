class Solution:
    def reverse(self, x: int) -> int:
        if(x>= -2147483648 and x<= 2147483647):
            y = x
            x = str(x)
            flag = 0
            if(x[0] == "-"):
                z = x[0]
                flag = 1
                x = x[1:]
            x = x[::-1]
            length1 = 0
            for char in x:
                length1 += 1
            if(length1 >= 10 and flag == '-'):
                return 0
            for i in range(0,length1):
                if(x[0]=='0'):
                    x = x[1:]
                    length2 = 0
                    for char in x:
                        length2 += 1
                    if(length2>0):
                        if(x[0]>'0' and x[0]<='9'):
                            break
            if (flag==1):
                x =z + x
            
            if(x!=''):
                x = int(x)
                if(x>= -2147483648 and x<= 2147483647):
                    return x
                else:
                    return 0
            else:
                return int(0)
        else:
            return 0