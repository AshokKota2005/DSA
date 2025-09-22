class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        d = {'a' : ".-",'b' : "-...",'c' : "-.-.",'d' : "-..",'e' : ".",'f' : "..-.",'g' : "--.",'h' : "....",'i' : "..",'j' : ".---",'k' : "-.-",'l' : ".-..",'m' : "--",'n' : "-.",'o' : "---",'p' : ".--.",'q' : "--.-",'r' : ".-.",'s' : "...",'t' : "-",'u' : "..-",'v' : "...-",'w' : ".--",'x' : "-..-",'y' : "-.--",'z' : "--.."}
        list1 = []
        for char in words:
            res = ""
            for i in range(0,len(char)):
                res = res + d[char[i]]
            list1.append(res)
        return len(set(list1))
       


        
        