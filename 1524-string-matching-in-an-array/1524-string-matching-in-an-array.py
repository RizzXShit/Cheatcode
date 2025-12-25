class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=[]
        
        for i in words:
            for j in words:
                if i in j and i!=j:
                    a.append(i)
        return list(set(a))
        