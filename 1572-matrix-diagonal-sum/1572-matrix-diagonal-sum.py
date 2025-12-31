class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        k=0
        su=0
        m=len(mat[0])-1
        for i in mat:
            su+=i[k]
            k+=1
        for j in mat:
            su+=j[m]
            m-=1
        if len(mat)%2!=0:
            return su-(mat[((len(mat)+1)/2)-1][((len(mat)+1)/2)-1])
        return su


        