class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        live = []
        dead = []
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                count = 0
                if 0 <= i-1 < len(board):
                    if board[i-1][j] == 1:
                        count += 1 
                if  0 <= i+1 < len(board):
                    if board[i+1][j] == 1:
                        count += 1
                if  0 <= j-1 < len(board[0]):
                    if board[i][j-1] == 1:
                        count += 1
                if  0 <= j+1 < len(board[0]):
                    if board[i][j+1] == 1:
                        count += 1
                if 0 <= i-1 < len(board) and 0 <= j-1 < len(board[0]):
                    if board[i-1][j-1] == 1:
                        count += 1
                if 0 <= i-1 < len(board) and 0 <= j+1 < len(board[0]):
                    if board[i-1][j+1] == 1:
                        count += 1
                if 0 <= i+1 < len(board) and 0 <= j-1 < len(board[0]):
                    if board[i+1][j-1] == 1:
                        count += 1
                if 0 <= i+1 < len(board) and 0 <= j+1 < len(board[0]):
                    if board[i+1][j+1] == 1:
                        count += 1
                if board[i][j] == 1:
                    if count < 2:
                        dead.append([i,j])
                    elif count > 3:
                        dead.append([i,j])
                else:
                    if count == 3:
                        live.append([i,j])
        for char in dead:
            board[char[0]][char[1]] = 0
        for char in live:
            board[char[0]][char[1]] = 1   
        """
        Do not return anything, modify board in-place instead.
        """
        