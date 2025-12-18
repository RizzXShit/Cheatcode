class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        a=0
        n = len(mat)
        c=[]
        c.append(mat)
        def rotate(mat):
            
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            for row in mat:
                row.reverse()
            
            return mat
                
        while a<4:
            mat=rotate([row[:] for row in mat])
            c.append(mat)
            a+=1
        return target in c

        