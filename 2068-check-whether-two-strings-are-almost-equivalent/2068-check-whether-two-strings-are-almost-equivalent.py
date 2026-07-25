class Solution(object):
    def checkAlmostEquivalent(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return all(v < 4 for v in ((Counter(w1) - Counter(w2)) + (Counter(w2) - Counter(w1))).values())