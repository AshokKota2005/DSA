class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        diffs = []
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                diffs.append(int(i))
        if len(diffs) == 2:
            if s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]:
                return True
        return False

        