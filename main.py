import pygame as py
import grid
import algoritm
import button
import hearts
import screens
py.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GRID_SIZE = 450

py.display.set_caption('Sudoku')
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screens_start = screens.Screens()

hearts = hearts.Hearts(6, screen)
grid_x = (SCREEN_WIDTH - GRID_SIZE) // 2
grid_y = (SCREEN_HEIGHT - GRID_SIZE) // 2

game_grid = grid.Grid(9, 9, GRID_SIZE, GRID_SIZE,hearts)
one = py.image.load('Numbers/1.png').convert_alpha()
two = py.image.load('Numbers/2.png').convert_alpha()
three = py.image.load('Numbers/3.png').convert_alpha()
four = py.image.load('Numbers/4.png').convert_alpha()
five = py.image.load('Numbers/5.png').convert_alpha()
six = py.image.load('Numbers/6.png').convert_alpha()
seven = py.image.load('Numbers/7.png').convert_alpha()
eight = py.image.load('Numbers/8.png').convert_alpha()
nine = py.image.load('Numbers/9.png').convert_alpha()

start = py.image.load('Buttons/start.png').convert_alpha()
exit_ = py.image.load('Buttons/exit.png').convert_alpha()

one_button = button.Button(40, 40, one, screen, 0.35,game_grid,1)
two_button = button.Button(110, 43, two, screen, 0.35,game_grid,2)
three_button = button.Button(200, 40, three, screen, 0.35,game_grid,3)
four_button = button.Button(280, 43, four, screen, 0.35,game_grid,4)
five_button = button.Button(358, 45, five, screen, 0.35,game_grid,5)
six_button = button.Button(445, 40, six, screen, 0.35,game_grid,6)
seven_button = button.Button(520, 43, seven, screen, 0.35,game_grid,7)
eight_button = button.Button(600, 45, eight, screen, 0.35,game_grid,8)
nine_button = button.Button(680, 43, nine, screen, 0.35,game_grid,9)

start_button = button.Button(250,600, start, screen, 0.5,None,None)
exit_button = button.Button(390,602, exit_, screen, 0.5,None,None)




algoritm = algoritm.Algoritm(game_grid.grid_return())
game_grid.set_algorithm(algoritm)
algoritm.fill_board()
algoritm.remove_numbers()
game_grid.refresh()

running = True


while running:
    screen.fill((240, 240, 240))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            running_2 = False



    hearts.draw()
    game_grid.draw(screen)
    one_button.place_number()
    two_button.place_number()
    three_button.place_number()
    four_button.place_number()
    five_button.place_number()
    six_button.place_number()
    seven_button.place_number()
    eight_button.place_number()
    nine_button.place_number()




    if start_button.draw():
        algoritm.reset()
        game_grid.refresh()


    if exit_button.draw():
        running = False
        running_2 = False
        py.quit()


    py.display.update()
py.quit()