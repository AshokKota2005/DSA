class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            list1 = i.split(' ')
            if len(list1) > res:
                res = len(list1)
        return res
        