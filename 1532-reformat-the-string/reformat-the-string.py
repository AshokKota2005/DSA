class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        digits = []
        for char in s:
            if char.isalpha():
                alpha.append(char)
            elif char.isdigit():
                digits.append(char)
        print(alpha)
        print(digits)
        if len(alpha) == len(digits) or len(alpha) == len(digits)-1 or len(digits) == len(alpha)-1:
            if len(alpha) >= len(digits):
                a = alpha
                b = digits
            else:
                a = digits
                b = alpha
            j = 0
            for i in range(1,2*len(a),2):
                if j != len(b):
                    a.insert(i,b[j])
                    j = j+1
            a = "".join(a)
            return a
        else:
            return ""


        