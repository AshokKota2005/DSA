class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s))<len(goal)
        diffs = []
        for i in range(len(s)):
            if(s[i] != goal[i]):
                diffs.append(int(i))
        
        if len(diffs) == 2:
            if s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]:
                return True
        
        return False

            