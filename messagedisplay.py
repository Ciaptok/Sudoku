import pygame as py


class MessageDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.font = py.font.Font(None, 36)
        self.message = None
        self.message_timer = 0
        self.display_time = 2000

    def show_message(self, message):
        self.message = message
        self.message_timer = py.time.get_ticks()

    def draw(self):
        if self.message:
            current_time = py.time.get_ticks()
            if current_time - self.message_timer < self.display_time:
                message_surface = self.font.render(self.message, True, (255, 0, 0))
                message_rect = message_surface.get_rect(center=(self.screen.get_width() // 2, 50))

                bg_rect = message_rect.inflate(20, 20)
                py.draw.rect(self.screen, (255, 255, 255), bg_rect)
                py.draw.rect(self.screen, (200, 200, 200), bg_rect, 2)

                self.screen.blit(message_surface, message_rect)
            else:
                self.message = None