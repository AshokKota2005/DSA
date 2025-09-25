class FrontMiddleBackQueue:

    def __init__(self):
        self.list1 = []
        
    def pushFront(self, val: int) -> None:
        self.list1 = self.list1[::-1]
        self.list1.append(val)
        self.list1 = self.list1[::-1]

    def pushMiddle(self, val: int) -> None:
        length = len(self.list1)
        length = length//2
        self.list1.insert(length,val)
        
    def pushBack(self, val: int) -> None:
        self.list1.append(val)
        
    def popFront(self) -> int:
        if len(self.list1) != 0:
            self.list1 = self.list1[::-1]
            res = self.list1.pop()
            self.list1 = self.list1[::-1] 
            return res
        else:
            return -1
        
    def popMiddle(self) -> int:
        if len(self.list1) != 0:
            length = len(self.list1) 
            length = ceil(length/2)-1
            res = self.list1.pop(length)
            return res
        else:
            return -1
        
    def popBack(self) -> int:
        if len(self.list1) != 0:
            res = self.list1.pop()
            return res
        else:
            return -1
        
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()