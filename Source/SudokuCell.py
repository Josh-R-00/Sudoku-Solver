class SudokuCell:

    def __init__(self, value):
        if value == 0:
            self.value = 0
            self.potentials = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.value = value
            self.potentials = []

    def clear_cell(self, value):
        if value in self.potentials:
            self.potentials.remove(value)

    def print(self):
        print(self.value, self.potentials, sep = '      ')
