class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        f_row = ['q','w','e','r','t','y','u','i','o','p']
        s_row = ['a','s','d','f','g','h','j','k','l']
        t_row = ['z','x','c','v','b','n','m']
        for char in words:
            flag = True 
            check = char[0].lower() 
            if check in f_row:
                for j in range(0,len(char)):
                    if char[j].lower() not in f_row:
                        flag = False
                        break
            elif check in s_row: 
                for j in range(0,len(char)):
                    if char[j].lower() not in s_row:
                        flag = False
                        break
            elif check in t_row:
                for j in range(0,len(char)):
                    if char[j].lower() not in t_row:
                        flag = False
                        break
            if flag == True:
                result.append(char)
        return result