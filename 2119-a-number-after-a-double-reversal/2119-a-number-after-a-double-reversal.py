class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        if len(num) == 1:
            return True
        m = num
        m = m[::-1]
        while m[0] == '0':
            m = m[1:]
        m = m[::-1]
        if m == num:
            return True 
        else:
            return False

        