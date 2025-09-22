class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ele = strs[0]
        for i in range(0,len(strs)):
            if len(strs[i]) < len(ele):
                ele = strs[i]
        res = ""
        for i in range(0,len(ele)):
            flag = True
            for j in range(0,len(strs)):
                if ele[i] != strs[j][i]:
                    flag = False
                    break
            if flag == True:
                res = res + ele[i]
            else:
                break
        return res



        