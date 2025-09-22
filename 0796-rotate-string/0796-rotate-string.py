class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i,char in enumerate(s):
            s+=s[0]
            #print(s)
            s=s[1:]
            #print(s)
            if s==goal:
                return True
        return False