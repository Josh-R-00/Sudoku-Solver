from tkinter import filedialog
from tkinter import *
from SudokuObject import *
import time

numberlist = None
sudokuObj = None


def fileUpload():
    global numberlist
    global sudokuObj

    if sudokuObj is not None:
        sudokuObj = None

    filepath = filedialog.askopenfile(initialdir="/", title="Select Sudoku File")
    print(filepath.name)
    data = open(filepath.name)
    numberlist = data.read().splitlines()
    sudokuObj = SudokuObject(numberlist)
    sudokuObj.clear()
    update()


def solve():
    global sudokuObj
    sudokuObj.solve()
    update()


def solveAll():
    global sudokuObj
    while sudokuObj.solve():
        update()


def update():
    global sudokuObj

    for x in range(9):
        for y in range(9):
            value = sudokuObj.cellgrid[x][y].value
            if value != 0:
                sudokuGrid.create_text((y * 60) + 80, (x * 60) + 80, text=value, font="Times 18")


master = Tk()

sudokuGrid = Canvas(master, width=640, height=640)
sudokuGrid.grid(row=1, column=0, padx=10, pady=0)

sudokuGrid.create_rectangle(50, 50, 590, 590, fill="white", width=5)
for x in range(0, 540, 180):
    sudokuGrid.create_line((50 + x), 50, (50 + x), 590, width=5)
    sudokuGrid.create_line(50, (50 + x), 590, (50 + x), width=5)
    for y in range(60, 180, 60):
        sudokuGrid.create_line((50 + x + y), 50, (50 + x + y), 590, width=1)
        sudokuGrid.create_line(50, (50 + x + y), 590, (50 + x + y), width=1)

buttonFrame = Frame(width=100, height=200, relief=RAISED)
buttonFrame.grid(row=1, column=1, padx=(0, 50), pady=10)

fileUploadButton = Button(buttonFrame, text="Choose Sudoku File", command=fileUpload)
fileUploadButton.grid(row=1, column=0, pady=10)

fileSolveButton = Button(buttonFrame, text="Solve Pass", command=solve)
fileSolveButton.grid(row=2, column=0, pady=10)

fileSolveButton = Button(buttonFrame, text="Solve All", command=solveAll)
fileSolveButton.grid(row=3, column=0, pady=10)

titleText = Label(text="Sudoku Solver", font="Times 30")
titleText.grid(row=0, column=0, pady=(10, 0))

master.mainloop()

# for x in range(0, 9, 1):
#     for y in range(0, 9, 1):
#         sudokuGrid.create_text((x * 60) + 60, (y * 60) + 110, text="1", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 80, (y * 60) + 110, text="2", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 50, (y * 60) + 110, text="3", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 60, (y * 60) + 130, text="4", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 80, (y * 60) + 130, text="5", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 50, (y * 60) + 130, text="6", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 60, (y * 60) + 150, text="7", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 80, (y * 60) + 150, text="8", font="Times 12")
#         sudokuGrid.create_text((x * 60) + 50, (y * 60) + 150, text="9", font="Times 12")
