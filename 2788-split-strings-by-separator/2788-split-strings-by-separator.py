class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        a=[]
        for i in words:
            b=i.split(separator)
            while "" in b:
                b.remove("")
            a.extend(b)
        return a

        