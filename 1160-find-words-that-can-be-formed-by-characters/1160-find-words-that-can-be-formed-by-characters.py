class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for i in range(0,len(words)):
            temp = chars
            flag = False
            for j in range(0,len(words[i])):
                if words[i][j] in temp:
                    temp = temp.replace(words[i][j],"",1)
                else:
                    flag = True
                    break
            if flag == False:
                res = res + len(words[i])
        return res
        