class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length = 0
        for char in arr:
            length += 1
        for i in range(0,length):
            for j in range(0,length):
                if(i != j and arr[i] == 2*arr[j]):
                    return True
        return False
        