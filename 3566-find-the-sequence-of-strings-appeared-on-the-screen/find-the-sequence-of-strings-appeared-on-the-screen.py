class Solution:
    def stringSequence(self, target: str) -> List[str]:
        d = {'a':'b',"b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
        result = []
        res = ""
        for i in range(0,len(target)):
            res = res + 'a'
            while res[-1] != target[i]:
                result.append(res) 
                char = d[res[-1]]
                res = res[:-1]
                res = res + char
            if res[-1] == target[i]:
                result.append(res)
        return result