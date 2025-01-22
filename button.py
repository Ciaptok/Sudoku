import pygame as pd

class Button:
    def __init__(self,x,y,image,screen,scale,game_grid,number):
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pd.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.screen = screen
        self.clicked = False
        self.game_grid = game_grid
        self.number = number


    def draw(self):
        action = False
        pos = pd.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pd.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if pd.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.screen.blit(self.image,(self.x,self.y))

        return action

    def place_number(self):
        if self.draw():
            if self.number is not None:
                self.game_grid.place_number(self.number)

