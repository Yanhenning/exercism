class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(number) for number in row.split()] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [number[index - 1] for number in self.matrix]
