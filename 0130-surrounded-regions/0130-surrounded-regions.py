class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                board[i][j]="X"
        