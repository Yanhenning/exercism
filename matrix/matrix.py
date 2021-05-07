from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = [[int(number) for number in row.split()] for row in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        return [number for number in self.matrix[index - 1]]

    def column(self, index: int) -> List[int]:
        return [number[index - 1] for number in self.matrix]
