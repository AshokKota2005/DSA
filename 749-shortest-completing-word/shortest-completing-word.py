class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        list1 = []
        for i in range(0,len(licensePlate)):
            if licensePlate[i].isalpha():
                list1.append(licensePlate[i].lower())
        res = "eeeeeeeeeeeeeeeeeee"
        for char in words:
            flag = True
            word = char
            for i in range(0,len(list1)):
                if list1[i] in char:
                    char = char.replace(list1[i],"",1)
                    print(char)
                else:
                    flag = False
                    break
            char = word
            if flag == True and len(char) < len(res):
                res = char
        return res


        


        