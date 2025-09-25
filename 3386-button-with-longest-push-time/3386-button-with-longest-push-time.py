class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        list1 = []
        list1.append(events[0][1]) 
        for i in range(0,len(events)-1):
            diff = events[i+1][1] - events[i][1] 
            list1.append(diff)
        list2 = []
        max1 = max(list1)  
        ind = list1.index(max1)
        list2.append(ind)
        list1[ind] = 0 
        for i in range(0,len(list1)):
            max2 = max(list1)
            if max2 == max1:
                ind1 = list1.index(max2)
                list2.append(ind1)
                list1[ind1] = 0
            else:
                break
        print(list2)
        if len(list2) == 1:
            return events[list2[0]][0]
        else:
            list3 = []
            for i in range(0,len(list2)):
                list3.append(events[list2[i]][0])
            return min(list3)
       
        