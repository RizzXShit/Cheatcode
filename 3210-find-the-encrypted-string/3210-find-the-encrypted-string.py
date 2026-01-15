class Solution:
    def getEncryptedString(self, c: str, k: int) -> str:
        a=k
        b=list(c)
        s=list(c)
        for i in range(len(s)):
            if a>=len(s):
                a%=len(s)
            b[i]=s[a]
            a+=1
        return "".join(b)
        