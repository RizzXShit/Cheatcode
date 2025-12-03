class Solution(object):
    def validStrings(self, n):
        ans=[]
        if n==1:
            return ["0","1"]
        for i in range(2**n):
            if i==0:
                continue
            if i==2:
                a="10"
                if len(a)==n-1:
                    b="0"
                    a=b+a
                
                    ans.append(a)
            elif (2**n)%i!=0:
                a=str(bin(i))[2:]
                if len(a)==n-1:
                    b="0"
                    a=b+a
                if len(a)==n:
                    ans.append(a)
        return ans