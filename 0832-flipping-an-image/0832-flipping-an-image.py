class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(0,len(image)):
            list1 = image[i] 
            list1 = list1[::-1]
            for j in range(0,len(list1)):
                if list1[j] == 0:
                    list1[j] = 1
                else:
                    list1[j] = 0
            image[i] = list1
        return image