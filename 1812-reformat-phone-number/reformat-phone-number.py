class Solution:
    def reformatNumber(self, number: str) -> str:
        i = 0
        while i < len(number):
            if number[i].isdigit():
                i = i+1
            else:
                number = number.replace(number[i],"",1)
        res = ""
        while len(number) > 4:
            res = res + number[:3] + '-'
            number = number[3:]
        if len(number) == 2 or len(number) == 3:
            res = res + number[:]
        elif len(number) == 4:
            res = res + number[:2] + '-' + number[2:]
        return res            

        