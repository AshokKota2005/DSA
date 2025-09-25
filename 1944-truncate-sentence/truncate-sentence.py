class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = s.split(" ")
        res = res[:k]
        res = " ".join(res)
        return res
        