class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        for i in range(0,len(dictionary)):
            for j in range(0,len(sentence)):
                k = sentence[j][:len(dictionary[i])]
                if k == dictionary[i]:
                    sentence[j] = dictionary[i]
        sentence = " ".join(sentence)
        return sentence
        