import pygame as py
import grid
import algoritm
import button
import hearts
import copy
import startscreen
import messagedisplay

py.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GRID_SIZE = 450

py.display.set_caption('Sudoku')
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_screen = startscreen.StartScreen(screen)
message_display = messagedisplay.MessageDisplay(screen)

number_images = {
    1: py.image.load('Numbers/1.png').convert_alpha(),
    2: py.image.load('Numbers/2.png').convert_alpha(),
    3: py.image.load('Numbers/3.png').convert_alpha(),
    4: py.image.load('Numbers/4.png').convert_alpha(),
    5: py.image.load('Numbers/5.png').convert_alpha(),
    6: py.image.load('Numbers/6.png').convert_alpha(),
    7: py.image.load('Numbers/7.png').convert_alpha(),
    8: py.image.load('Numbers/8.png').convert_alpha(),
    9: py.image.load('Numbers/9.png').convert_alpha()
}

start_img = py.image.load('Buttons/start.png').convert_alpha()
exit_img = py.image.load('Buttons/exit.png').convert_alpha()


def initialize_game(settings):
    hearts_obj = hearts.Hearts(settings["hearts"], screen)
    game_grid = grid.Grid(9, 9, GRID_SIZE, GRID_SIZE, hearts_obj)

    number_buttons = {
        1: button.Button(40, 40, number_images[1], screen, 0.35, game_grid, 1),
        2: button.Button(110, 43, number_images[2], screen, 0.35, game_grid, 2),
        3: button.Button(200, 40, number_images[3], screen, 0.35, game_grid, 3),
        4: button.Button(280, 43, number_images[4], screen, 0.35, game_grid, 4),
        5: button.Button(358, 45, number_images[5], screen, 0.35, game_grid, 5),
        6: button.Button(445, 40, number_images[6], screen, 0.35, game_grid, 6),
        7: button.Button(520, 43, number_images[7], screen, 0.35, game_grid, 7),
        8: button.Button(600, 45, number_images[8], screen, 0.35, game_grid, 8),
        9: button.Button(680, 43, number_images[9], screen, 0.35, game_grid, 9)
    }

    start_button = button.Button(250, 600, start_img, screen, 0.5, None, None)
    exit_button = button.Button(390, 602, exit_img, screen, 0.5, None, None)

    algoritm_obj = algoritm.Algoritm(game_grid.grid_return())
    game_grid.set_algorithm(algoritm_obj)
    algoritm_obj.fill_board()
    grid_solved = copy.deepcopy(game_grid.grid_return())
    algoritm_obj.remove_numbers(settings["difficulty"])
    game_grid.refresh()

    return game_grid, hearts_obj, number_buttons, start_button, exit_button, algoritm_obj


# Game state
game_state = "start"
game_settings = None
game_result = None
game_objects = None

# Main game loop
running = True
while running:
    if game_state == "start":
        difficulty_buttons, hearts_buttons, start_rect = start_screen.draw()

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    result = start_screen.handle_click(event.pos, difficulty_buttons, hearts_buttons, start_rect)
                    if result:
                        game_settings = result
                        game_objects = initialize_game(game_settings)
                        game_grid, hearts_obj, number_buttons, start_button, exit_button, algoritm_obj = game_objects
                        game_state = "game"

    elif game_state == "game":
        screen.fill((240, 240, 240))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        game_grid, hearts_obj, number_buttons, start_button, exit_button, algoritm_obj = game_objects

        hearts_obj.draw()
        game_grid.draw(screen)

        for button_obj in number_buttons.values():
            button_obj.place_number()

        # Handle game buttons
        if start_button.draw():
            algoritm_obj.reset()
            game_grid.refresh()
            hearts_obj.reset()
            message_display.show_message("Nowa gra rozpoczęta!")

        if exit_button.draw():
            game_state = "start"

        message_display.draw()

        if not hearts_obj.check_hearts():
            game_state = "end"
            game_result = False

        if game_grid.is_grid_complete():
            game_state = "end"
            game_result = True

    elif game_state == "end":
        button_rect = end_screen.draw(game_result)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if end_screen.handle_click(event.pos, button_rect):
                        game_state = "start"

    py.display.update()

py.quit()