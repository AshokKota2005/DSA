class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        a,b = "",""
        i = 0
        while i < 4:
            min1 = min(num)
            num = num.replace(min1,"",1)
            if i%2 == 0:
                a = a+min1
            else:
                b = b+min1
            i = i+1
        return int(a)+int(b)

        