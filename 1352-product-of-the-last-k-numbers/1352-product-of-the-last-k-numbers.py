
import math
class ProductOfNumbers:
    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)
    

    def getProduct(self, k: int) -> int:
        temp = self.nums[-k:]
        sum1 = math.prod(temp)
        return sum1
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)