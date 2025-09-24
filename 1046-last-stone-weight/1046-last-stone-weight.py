class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            if len(stones) == 0:
                return 0
            stones.sort(reverse = True)
            a = stones[0]
            stones.pop(0)
            b = stones[0]
            stones.pop(0)
            if a != b:
                stones.append(abs(a-b))
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

        