class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        for i in range(0,len(password)-1):
            if password[i] == password[i+1]:
                return False
        if len(password) >= 8:
            upper,lower,digit,spe_char = 0,0,0,0
            for i in range(0,len(password)):
                if password[i] >= 'a' and password[i] <= 'z':
                    lower += 1
                elif password[i] >= 'A' and password[i] <= 'Z':
                    upper += 1
                elif password[i] >= '0' and password[i] <= '9':
                    digit += 1
                else:
                    spe_char += 1
            if lower >= 1 and upper >= 1 and digit >=1 and spe_char >= 1:
                return True
            else:
                return False
        else:
            return False
        