class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0 and  i == 0:
                if i+1 < len(flowerbed) and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n = n-1
            elif flowerbed[i] == 0 and i == len(flowerbed)-1:
                if flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n = n-1
            elif flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n = n-1
        if n <= 0:
            return True
        else:
            return False
             

        