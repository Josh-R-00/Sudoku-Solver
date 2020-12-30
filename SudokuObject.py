from SudokuCell import *
import time

class SudokuObject:

    def __init__(self, sudokuIntake):
        self.solved = False
        self.cellgrid = []
        self.rowValues = []
        self.colValues = []
        self.boxValues = []

        for row in sudokuIntake:
            rowlist = []
            for col in row:
                sudokucell = SudokuCell(int(col))
                rowlist.append(sudokucell)
            self.cellgrid.append(rowlist)

        self.rowValues = self.cellgrid

        for col in range(9):
            column = []
            for val in range(9):
                column.append(self.cellgrid[val][col])
            self.colValues.append(column)

        box1 = []; box2 = []; box3 = []
        for firstRow in range(3):
            for firstCol in range(3):
                box1.append(self.cellgrid[firstRow][firstCol])
            for secondCol in range(3,6):
                box2.append(self.cellgrid[firstRow][secondCol])
            for thirdCol in range (6,9):
                box3.append(self.cellgrid[firstRow][thirdCol])
        self.boxValues.append(box1)
        self.boxValues.append(box2)
        self.boxValues.append(box3)

        box1.clear(); box2.clear(); box3.clear()

        for secondRow in range(3,6):
            for firstCol in range(3):
                box1.append(self.cellgrid[secondRow][firstCol])
            for secondCol in range(3, 6):
                box2.append(self.cellgrid[secondRow][secondCol])
            for thirdCol in range(6, 9):
                box3.append(self.cellgrid[secondRow][thirdCol])
            self.boxValues.append(box1)
            self.boxValues.append(box2)
            self.boxValues.append(box3)

        box1.clear(); box2.clear(); box3.clear()

        for thirdRow in range(6,9):
            for firstCol in range(3):
                box1.append(self.cellgrid[thirdRow][firstCol])
            for secondCol in range(3, 6):
                box2.append(self.cellgrid[thirdRow][secondCol])
            for thirdCol in range(6, 9):
                box3.append(self.cellgrid[thirdRow][thirdCol])
            self.boxValues.append(box1)
            self.boxValues.append(box2)
            self.boxValues.append(box3)

        box1.clear(); box2.clear(); box3.clear()


    def print(self):
        for row in self.cellgrid:
            for col in row:
                print(col.value, end = '')
            print()

    def clearBox(self, row, col, value):
        row = (row // 3) * 3
        col = (col // 3) * 3
        rowend = row + 3
        colend = col + 3

        for x in range(row, rowend):
            for y in range(col, colend):
                self.cellgrid[x][y].clear_cell(value)


    def clearColumn(self, col, value):
        for row in range(9):
            self.cellgrid[row][col].clear_cell(value)

    def clearRow(self, row, value):
        for col in range(9):
            self.cellgrid[row][col].clear_cell(value)

    def clear(self):
        for row in range(9):
            for col in range(9):
                value = self.cellgrid[row][col].value
                if value != 0:
                    self.clearBox(row, col, value)
                    self.clearColumn(col, value)
                    self.clearRow(row, value)

    def solveOneChoice(self):
        work = False
        for row in range(9):
            for col in range(9):
                if len(self.cellgrid[row][col].potentials) == 1:
                    newvalue = self.cellgrid[row][col].potentials.pop(0)
                    self.cellgrid[row][col].value = newvalue
                    work = True
        self.clear()
        return work

    def solveElimination(self):
        work = False
        for val in range(9):
            once = False
            multiple = False
            cell = None

            for row in self.rowValues:
                for sudokuCell in row:
                    if sudokuCell.value != 0: continue
                    if val in sudokuCell.potentials and once == False:
                        once = True
                        cell = sudokuCell
                    elif val in sudokuCell.potentials and once == True:
                        multiple = True
                if once == True and multiple == False:
                    cell.value = val
                    cell.potentials.clear()
                    work = True
                once = False; multiple = False; cell = None; self.clear()

            for col in self.colValues:
                for sudokuCell in col:
                    if sudokuCell.value != 0: continue
                    if val in sudokuCell.potentials and once == False:
                        once = True
                        cell = sudokuCell
                    elif val in sudokuCell.potentials and once == True:
                        multiple = True
                if once == True and multiple == False:
                    cell.value = val
                    cell.potentials.clear()
                    work = True
                once = False; multiple = False; cell = None; self.clear()

            for box in self.boxValues:
                for sudokuCell in box:
                    if sudokuCell.value != 0: continue
                    if val in sudokuCell.potentials and once == False:
                        once = True
                        cell = sudokuCell
                    elif val in sudokuCell.potentials and once == True:
                        multiple = True
                if once == True and multiple == False:
                    cell.value = val
                    cell.potentials.clear()
                    work = True

        self.clear()
        return work

    def solve(self):
        if self.solveOneChoice(): return True
        elif self.solveElimination(): return True
        else: return False
