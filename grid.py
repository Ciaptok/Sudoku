import pygame as py
import small_square


class Grid:
    def __init__(self, rows, cols, width, height, hearts):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.cell_width = width // cols
        self.cell_height = height // rows
        self.squares = [[None for _ in range(cols)] for _ in range(rows)]
        self.selected_row = None
        self.selected_col = None
        self.running = True
        self._init_squares()
        self.hearts = hearts
        self.game_ended = False

    def _init_squares(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j] = small_square.SmallSquare(
                    self.board[i][j],
                    j * self.cell_width,
                    i * self.cell_height,
                    self.cell_width,
                    self.cell_height,
                    None
                )

    def clear_highlights(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].selected = False
                self.squares[i][j].secondary_selected = False

    def highlight_row_col(self, row, col, value):
        self.clear_highlights()
        if row is not None and col is not None:
            self.squares[row][col].selected = True
            for j in range(self.cols):
                if j != col:
                    self.squares[row][j].secondary_selected = True
            for i in range(self.rows):
                if i != row:
                    self.squares[i][col].secondary_selected = True
            if value:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.squares[i][j].value == value:
                            self.squares[i][j].selected = True

    def draw(self, screen):
        if self.game_ended:
            return

        screen_width = self.width + 40
        screen_height = self.height + 40
        surface = py.Surface((screen_width, screen_height))
        surface.fill((240, 240, 240))
        py.draw.rect(surface, 'white', (20, 20, self.width, self.height))

        for i in range(self.rows):
            for j in range(self.cols):
                square = self.squares[i][j]
                square.screen = surface
                square.x = j * self.cell_width + 20
                square.y = i * self.cell_height + 20
                if square.draw():
                    self.selected_row = i
                    self.selected_col = j
                    value_selected = self.squares[i][j].value
                    self.highlight_row_col(i, j, value_selected)

        for i in range(10):
            thickness = 6 if i % 3 == 0 else 1
            py.draw.line(surface, (0, 0, 0),
                         (i * self.width // 9 + 20, 20),
                         (i * self.width // 9 + 20, self.height + 20), thickness)
            py.draw.line(surface, (0, 0, 0),
                         (20, i * self.height // 9 + 20),
                         (self.width + 20, i * self.height // 9 + 20), thickness)

        screen.blit(surface, ((screen.get_width() - screen_width) // 2,
                              (screen.get_height() - screen_height) // 2))

    def grid_return(self):
        return self.board

    def refresh(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].value = self.board[i][j]
                self.squares[i][j].color = (255, 255, 255)
                self.squares[i][j].selected = False
        self.selected_row = None
        self.selected_col = None
        self.game_ended = False
        self.draw(py.display.get_surface())
        py.display.update()

    def place_number(self, number):
        if self.game_ended:
            return False

        if self.selected_row is not None and self.selected_col is not None:
            if self.algorithm.is_valid(self.selected_row, self.selected_col, number):
                self.squares[self.selected_row][self.selected_col].value = number
                self.board[self.selected_row][self.selected_col] = number
                if self.is_grid_complete():
                    self.show_end_screen(True)
                return True
            else:
                if self.squares[self.selected_row][self.selected_col].value:
                    print("Nie można zmienić tej komórki!")
                else:
                    if not self.hearts.remove_heart():
                        self.show_end_screen(False)
                    print("Niepoprawny ruch!")
        else:
            print("Nie wybrano komórki!")
        return False

    def return_selected(self):
        if self.selected_row is not None and self.selected_col is not None:
            return (self.selected_row, self.selected_col)
        return None

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def is_grid_complete(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def show_end_screen(self, won):
        self.game_ended = True
        screen = py.display.get_surface()
        screen.fill((0, 0, 0))

        font = py.font.Font(None, 74)

        if won:
            message = "GRATULACJE!"
            submessage = "Rozwiązałeś Sudoku!"
            color = (255, 215, 0)
        else:
            message = "KONIEC GRY!"
            submessage = "Skończyły się życia!"
            color = (255, 0, 0)

        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
        screen.blit(text, text_rect)

        small_font = py.font.Font(None, 36)
        subtext = small_font.render(submessage, True, (255, 255, 255))
        subtext_rect = subtext.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(subtext, subtext_rect)

        button_font = py.font.Font(None, 48)
        button_text = button_font.render("Naciśnij SPACJĘ aby wrócić do menu", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() * 2 // 3))
        screen.blit(button_text, button_rect)

        py.display.flip()


        waiting = True
        while waiting:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    return
                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        waiting = False
                        self.reset_game()
                        import main
                        main.game_state = "start"
                        return

    def reset_game(self):
        self.game_ended = False
        self.hearts.reset()
        self.refresh()

    def check_running(self):
        return not self.game_ended