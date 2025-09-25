class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        length = len(pref)
        for i in range(0,len(words)):
            if pref in words[i] and length <= len(words[i]):
                check = words[i][:length]
                if check == pref:
                    count = count + 1
        return count
                

        