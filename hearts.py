import pygame as py

class Hearts:
    def __init__(self, numbers, screen):
        self.numbers = numbers
        self.screen = screen
        self.hearts = [1] * self.numbers

        self.full_heart = py.transform.scale(py.image.load('heart/fill.png').convert_alpha(), (50, 50))
        self.empty_heart = py.transform.scale(py.image.load('heart/nofill.png').convert_alpha(), (50, 50))

    def draw(self):
        for index, heart in enumerate(self.hearts):
            x = 60
            y = 150 + index * 60
            if heart == 1:
               self.screen.blit(self.full_heart, (x, y))
            else:
                self.screen.blit(self.empty_heart, (x, y))

    def remove_heart(self):
        if sum(self.hearts) == 1:
            for i in range(len(self.hearts)):
                if self.hearts[i] == 1:
                    self.hearts[i] = 0
                    break
            return False
        for i in range(len(self.hearts)):
            if self.hearts[i] == 1:
                self.hearts[i] = 0
                break
        return True

    def reset(self):
        self.hearts = [1] * self.numbers

    def check_hearts(self):
        return sum(self.hearts) > 0
