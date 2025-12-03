class Solution(object):
    def validStrings(self, n):
        ans = []
        for i in range(2**n):
            s = bin(i)[2:].zfill(n)   
            if "00" not in s:       
                ans.append(s)
        return ans
