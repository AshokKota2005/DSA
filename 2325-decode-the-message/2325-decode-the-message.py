class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        k = 97
        for i in range(0,len(key)):
            if key[i] not in d.keys() and key[i].isalpha():
                d[key[i]] = chr(k)
                k = k+1
        res = ""
        for i in range(0,len(message)):
            if message[i].isalpha():
                res = res + d[message[i]]
            else:
                res = res + " "
        return res

        