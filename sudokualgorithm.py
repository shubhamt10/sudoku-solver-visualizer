import time

def canPlace(board,i,j,number):
    for k in range(0,9):
        if board[i][k] == number or board[k][j] == number:
            return False

    sr = i//3
    sc = j//3
    rn = 3
    sr = sr*3
    sc = sc*3

    for y in range(sr,sr+rn):
        for x in range(sc,sc+rn):
            if board[y][x] == number:
                return False

    return True

def sodokuSolver(board,i,j,drawBoard):
    if i==9:
        return True

    if j==9:
        return sodokuSolver(board,i+1,0,drawBoard)

    if not board[i][j] == 0:
        return sodokuSolver(board,i,j+1,drawBoard)
    
    for number in range(1,10):
        if canPlace(board,i,j,number):
            board[i][j] = number
            drawBoard(board,i,j)
            time.sleep(0.2)
            checkNext = sodokuSolver(board,i,j+1,drawBoard)
            if checkNext:
                return True
    

    board[i][j] = 0
    return False

