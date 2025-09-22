class MyHashSet:

    def __init__(self):
        self.result = []
        

    def add(self, key: int) -> None:
        self.result.append(key)
        

    def remove(self, key: int) -> None:
        self.result = [i for i in self.result if i != key] 
  
        

    def contains(self, key: int) -> bool:
        if key in self.result:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)