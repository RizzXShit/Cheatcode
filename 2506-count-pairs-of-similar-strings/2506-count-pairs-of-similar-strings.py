class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt=0
        for i in range(len(words)):
            words[i]=set(words[i])
        for i in range(len(words)): 
            for j in range(i+1, len(words)): 
                if words[i] == words[j]: 
                    cnt += 1
        return cnt
        