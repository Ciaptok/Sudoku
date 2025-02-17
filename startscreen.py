import pygame as py


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = py.font.Font(None, 48)
        self.small_font = py.font.Font(None, 36)


        self.difficulties = {
            "Łatwy": 20,
            "Średni": 40,
            "Trudny": 62
        }
        self.selected_difficulty = "Średni"


        self.hearts_options = [3, 4, 5, 6]
        self.selected_hearts = 6


        self.button_color = (100, 100, 255)
        self.selected_color = (50, 50, 200)
        self.text_color = (255, 255, 255)

    def draw_button(self, text, rect, selected=False):
        color = self.selected_color if selected else self.button_color
        py.draw.rect(self.screen, color, rect)
        text_surface = self.small_font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
        return rect

    def draw(self):
        self.screen.fill((240, 240, 240))

        title = self.font.render("SUDOKU", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title, title_rect)

        diff_title = self.small_font.render("Wybierz poziom trudności:", True, (0, 0, 0))
        self.screen.blit(diff_title, (200, 200))

        difficulty_buttons = {}
        for i, diff in enumerate(self.difficulties.keys()):
            rect = py.Rect(200 + i * 150, 250, 120, 40)
            difficulty_buttons[diff] = self.draw_button(diff, rect, diff == self.selected_difficulty)

        hearts_title = self.small_font.render("Wybierz liczbę żyć:", True, (0, 0, 0))
        self.screen.blit(hearts_title, (200, 350))

        hearts_buttons = {}
        for i, hearts in enumerate(self.hearts_options):
            rect = py.Rect(200 + i * 100, 400, 80, 40)
            hearts_buttons[hearts] = self.draw_button(str(hearts), rect, hearts == self.selected_hearts)

        start_rect = py.Rect(300, 500, 200, 50)
        start_button = self.draw_button("Rozpocznij grę", start_rect)

        return difficulty_buttons, hearts_buttons, start_rect

    def handle_click(self, pos, difficulty_buttons, hearts_buttons, start_rect):
        for diff, rect in difficulty_buttons.items():
            if rect.collidepoint(pos):
                self.selected_difficulty = diff
                return None

        for hearts, rect in hearts_buttons.items():
            if rect.collidepoint(pos):
                self.selected_hearts = hearts
                return None

        if start_rect.collidepoint(pos):
            return {
                "difficulty": self.difficulties[self.selected_difficulty],
                "hearts": self.selected_hearts
            }

        return None