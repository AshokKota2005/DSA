class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            k = 0
        elif ruleKey == 'color':
            k = 1
        elif ruleKey == 'name':
            k = 2
        c = 0
        for i in range(0,len(items)):
            if ruleValue == items[i][k]:
                c = c+1
        return c
