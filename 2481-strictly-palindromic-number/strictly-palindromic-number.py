class Solution(object):
    def isStrictlyPalindromic(self, n):
        for i in range(2,n-1):
            sum1 = ""
            temp = n
            while temp != 0:
                rem = temp%i
                sum1 = sum1 + str(rem)
                temp = temp//i
            if sum1 != sum1[::-1]:
                return False
        return True