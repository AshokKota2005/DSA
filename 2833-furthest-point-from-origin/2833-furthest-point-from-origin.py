class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        output = 0
        l = moves.count('L')
        r = moves.count('R')
        h = moves.count('_') 
        if l == r or l >= r:
            l = l+h-r
            return l
        else:
            r = r+h-l
            return r