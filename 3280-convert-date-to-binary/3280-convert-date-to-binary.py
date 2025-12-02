class Solution(object):
    def convertDateToBinary(self, date):
        a=date.split("-")
        b=""
        for i in a:
            c=bin(int(i))
            b+=str(c)[2:]
            b+="-"
        
        return b[0:-1:1]