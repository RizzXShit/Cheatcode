class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while True:
            a=str(i)
            if i>=10:
                p=int(a[0])*int(a[1])
            else:
                p=i
            if p%t==0:
                return i
            i+=1
            
        