def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    if row < 2 or col < 2:
        return 1
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != 0:
                board[i][j] = min(min(board[i-1][j], board[i][j-1]), board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))