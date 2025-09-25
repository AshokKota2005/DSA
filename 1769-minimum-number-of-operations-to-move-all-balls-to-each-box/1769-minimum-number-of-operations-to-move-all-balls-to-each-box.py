class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(0,len(boxes)):
            c = 0
            for j in range(0,len(boxes)):
                if boxes[j] == '1':
                    c = c + abs(i - j) 
            res.append(c)
        return res

        