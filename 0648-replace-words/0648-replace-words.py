class Solution(object):
    def replaceWords(self, dictionary, sentence):
    
        a = sentence.split()
        for i in range(len(dictionary)):
            for j in range(len(a)):
                if a[j].startswith(dictionary[i]):
                    a[j] = dictionary[i]
        return " ".join(a)
