from tkinter import *
from tkinter.ttk import *
from sudokualgorithm import sodokuSolver

root = Tk()
root.title("Sudoku Solver")
root.maxsize(800,800)
root.config(bg="black")

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def drawBoard(board,p,q):
    canvas.delete("all")
    c_height = 560
    c_width = 560
    offset = 10
    w = c_width//9
    h = c_height//9
    for i in range(0, 10):
        x = offset + i*w
        y = offset + i*h
        canvas.create_line(x,offset,x,c_height+offset,width=3)
        canvas.create_line(offset,y,c_width+offset,y,width=3)

    for i in range(0,9):
        for j in range(0,9):
            canvas.create_text(offset+w/2 + j*w,offset+h/2 + i*h,text = str(board[i][j]), 
                                font = ("Arial",20),fill=('green' if (i==p and j==q) else 'orange'))

    root.update_idletasks()

def start():
    global board
    drawBoard(board,0,0)
    sodokuSolver(board,0,0,drawBoard)

frame = Frame(root, height = 200, width = 600)
frame.grid(row = 0,column = 0, padx = 10,pady = 10)
startbtn = Button(frame, text = "Start", command = start)
startbtn.pack()

canvas = Canvas(root, height = 600,width = 600,bg='white')
canvas.grid(row = 1,column = 0, padx = 10, pady = 10)

root.mainloop()