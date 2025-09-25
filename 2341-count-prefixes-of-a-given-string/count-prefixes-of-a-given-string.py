class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        length = len(s)
        for i in range(0,len(words)):
            if words[i] in s and len(words[i]) <= length:
                check = s[:len(words[i])]
                if check == words[i]:
                    count = count + 1
        return count
        