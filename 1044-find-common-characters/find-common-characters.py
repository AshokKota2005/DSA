class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        ele = words[0]
        for char in ele:
            flag = True
            for i in range(0,len(words)):
                if char not in words[i]:
                    flag = False
                    break
                else:
                    words[i] = words[i].replace(char,"",1)   
            if flag == True:
                result.append(char)
        return result
        