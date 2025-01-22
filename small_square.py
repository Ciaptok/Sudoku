import pygame as pd


class SmallSquare:
    def __init__(self, value, x, y, width, height, screen):
        self.value = value
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.selected = False
        self.color = (255, 255, 255)
        self.clicked = False
        self.secondary_selected = False



    def draw(self):

        if self.selected:
            self.color = (200, 225, 255)
            border_thickness =  3
        elif self.secondary_selected:
            self.color = (200, 200, 200)
            border_thickness = 1
        else:
            self.color = (255, 255, 255)
            border_thickness = 1


        pd.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        border_color = (70, 70, 70) if not self.selected else (0, 100, 255)
        pd.draw.rect(self.screen, border_color, (self.x, self.y, self.width, self.height), border_thickness)

        action = False
        mouse_pos = pd.mouse.get_pos()

        main_screen = pd.display.get_surface()
        grid_x = (main_screen.get_width() - self.screen.get_width()) // 2
        grid_y = (main_screen.get_height() - self.screen.get_height()) // 2

        adjusted_x = mouse_pos[0] - grid_x
        adjusted_y = mouse_pos[1] - grid_y

        click_rect = pd.Rect(self.x, self.y, self.width, self.height)

        if click_rect.collidepoint(adjusted_x, adjusted_y):
            if pd.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
                self.selected = True
            elif pd.mouse.get_pressed()[0] == 0:
                self.clicked = False

        if not click_rect.collidepoint(adjusted_x, adjusted_y) and pd.mouse.get_pressed()[1]:
            self.selected = False

        if self.value != 0:
            font = pd.font.Font(None, int(self.width * 0.6))
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.x + self.width // 2 - text.get_width() // 2,
                                    self.y + self.height // 2 - text.get_height() // 2))

        return action


    def return_clicked(self):
        return self.value