class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        i = 0
        while i < len(paragraph):
            if paragraph[i] == ' ':
                i = i+1
            elif paragraph[i].isalpha(): 
                i = i+1
            else:
                paragraph = paragraph.replace(paragraph[i]," ")
        paragraph = paragraph.split(" ")
        print(paragraph)
        d = {}
        for char in paragraph:
            if char not in banned and char != "":
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
        print(d)
        res = ""
        result = 0
        for char in d.keys():
            if d[char] > result:
                result = d[char]
                res = char
        return res

        