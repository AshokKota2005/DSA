class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(start) > len(goal):
            goal = goal.zfill(len(start))
        else:
            start = start.zfill(len(goal))
        print(start)
        print(goal)
        for i in range(0,len(start)):
            if start[i] != goal[i]:
                c += 1
        return c    