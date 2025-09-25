class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        even,odd = [],[]
        for i in range(0,len(num)):
            if int(num[i])%2 == 0:
                even.append(num[i])
            else:
                odd.append(num[i])
        even.sort(reverse = True)
        odd.sort(reverse = True)
        res = [0]*len(num)
        a,b = 0,0
        for i in range(0,len(num)): 
            if int(num[i])%2 == 0:
                res[i] = even[a]   
                a = a+1
            else:
                res[i] = odd[b]
                b = b+1 
        res = "".join(res)
        res = int(res)
        return res

            
        