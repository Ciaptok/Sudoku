import pygame as py
import random

class Algoritm:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.solve =  None

    def print_board(self):
        for row in self.grid:
            print(row)

    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False

        for i in range(9):
            if self.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def fill_board(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    random_nums = random.sample(range(1, 10), 9)
                    for num in random_nums:
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.fill_board():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def remove_numbers(self, level=60):
        count = level
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.grid[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.grid[row][col] = 0
            count -= 1

    def reset(self):
        for row in range(9):
            for col in range(9):
                self.grid[row][col] = 0
        self.fill_board()
        self.remove_numbers()
