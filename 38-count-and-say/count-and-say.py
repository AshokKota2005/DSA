class Solution:
    def countAndSay(self, n: int) -> str:
        list1 = []
        for i in range(1,n+1):
            if len(list1) == 0:
                list1.append(1)
            elif len(list1) == 1:
                list1.insert(0,1)
            else:
                list2 = []
                c = 1
                for i in range(0,len(list1)-1): 
                    if list1[i] == list1[i+1]:
                        c = c+1
                    else:
                        list2.append(c)
                        list2.append(list1[i])
                        c = 1
                list2.append(c)
                list2.append(list1[i+1])
                list1 = list2
        list1 = list(map(str,list1))
        list1 = ''.join(list1)
        return list1
        