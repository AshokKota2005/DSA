class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        list1 = []
        for char in arr:
            c = 0
            for key in arr:
                if (key == char):
                    c = c+1
            if(c == 1):
                list1.append(char) 
        if(len(list1) < k):
            return ""
        else:
            return list1[k-1]

        