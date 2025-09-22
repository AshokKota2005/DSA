class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        binary = binary[::-1]
        res = int(binary,2)
        return res


        