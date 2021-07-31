import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from tkinter.constants import ANCHOR
import pygame
import random
import time
import tkinter
import canvas
from PIL import Image
from pygame import display
from pygame import font
from pygame.constants import NOEVENT
from pygame.version import PygameVersion

## ------------------------------------------------------
ROWS = 100
COLS = 100
WIDTH = 600
HEIGHT = 600

S_SPEED = 10  # Defining the speed of the snake

#Here I define my colors as CONSTANTS to use them anywhere in the code
B_WHITE = (255, 255, 255)
B_BLACK = (0, 0, 0)
APPLE = (255, 0, 0)
B_BLUE = (0, 0, 255)

GRID_SIZE = 20 #defining the size of the blocks, apple or snake
SNAKE_LIST = [] 
LENGTH_SNAKE = 1
## ------------------------------------------------------------

def main():
    #initiates pygame and opens up a window
    disp = background(display)

    clock = pygame.time.Clock()
    
    game_loop(disp, LENGTH_SNAKE, clock)
    



# def_grid(disp, GRID_SIZE)
    # text = font_of_score.render('Hello, World!!', True, B_WHITE)
    # textRect = text.get_rect()
    # textRect.center = (10,10)
    
    # while True:
    #     disp.blit(text, textRect)
        
def game_loop(disp, LENGTH_SNAKE, clock): ## ----------This creates the main purpose of the game
    
    game_over = False  # For open and close the game with need to know when the game is over
    close_game = False

    start_x = WIDTH / 2   #creating the coordinates
    start_y = HEIGHT / 2   #creating the coordinates

    x_change = 0
    y_change = 0
   
   #creating random coordinates for the apple to appear at
    foodx = round(random.randrange(0, WIDTH - GRID_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - GRID_SIZE) / 20.0) * 20.0
    

    while not game_over:
        
        while close_game == True:
            disp.fill(B_WHITE)
            image = pygame.image.load('pythonpic.png')
            disp.blit(image, (0, 0))
            pygame.display.update()
            message(disp)
            
            # the_score(length_snake - 1, None, None)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False
                    elif event.key == pygame.K_p:
                        game_over = False
                    game_loop(disp, LENGTH_SNAKE, clock)
                        
                    
        for event in pygame.event.get():
            #When pressing the close bottom, the game should be able to close.
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -GRID_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = GRID_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -GRID_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = GRID_SIZE
                    x_change = 0
        
        #Set the boundaries for the snake not to go beyond walls.
        if start_x >= WIDTH or start_x < 0 or start_y >= HEIGHT  or start_y < 0:
            message(disp)
            close_game = True
        
        start_x += x_change
        start_y += y_change
        disp.fill(B_BLACK)

        #Create a red apple and add it to the snake everytime the snake eats
        apple = pygame.draw.rect(disp, APPLE, [foodx, foody, GRID_SIZE, GRID_SIZE])
        snake_head = []
        snake_head.append(start_x)
        snake_head.append(start_y)
        SNAKE_LIST.append(snake_head)

        if len(SNAKE_LIST) > LENGTH_SNAKE:
            del SNAKE_LIST[0]

        for x in SNAKE_LIST[:-1]:
            if x == snake_head:
                close_game = True

        the_snake(GRID_SIZE, SNAKE_LIST, disp)
        # the_score(LENGTH_SNAKE - 1, None, None)
        
        pygame.display.update()
        
        if start_x == foodx and start_y == foody:
            num = LENGTH_SNAKE + 1
            print("Yumey!! Your Score is:", num)  ## This will display Yumey!! on the terminal everytime the snake eats to confirm that the apple has been eaten.
            # print("Your Score: " + str(the_score, None, None))
            foodx = round(random.randrange(0, WIDTH - GRID_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - GRID_SIZE) / 20.0) * 20.0
            LENGTH_SNAKE += 1

        clock.tick(S_SPEED) ## creating the speed of the snake
        
    pygame.quit()
    quit()

def message(disp):   ## ------A function that helps with adding text to the screen without having to repeat all code.
    font = pygame.font.SysFont(None, 50)  ## FONT_STYLE = pygame.font.SysFont("arial", 40)
                                        ## SysFont(name, size, bold=False, italic=False) -> Font
    text = font.render("Game Over", True, B_BLUE)
    disp.blit(text, [30, 30])   ## ----Coordinates of the text
    text = font.render("Press q to Quit", True, B_BLUE)
    disp.blit(text, [30, 60])
    pygame.display.update()
    time.sleep(2)

def welc_msg(disp):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Welcome to Snake Game", True, B_WHITE)
    disp.blit(text, [30, 30])

def the_score(score, disp, font_of_score):
    num = font_of_score.render('The Score is:', str(score), True, B_WHITE)
    disp.blit(num, [0, 0])

def the_snake(GRID_SIZE, snake_list, disp):
    for x in snake_list:
        pygame.draw.rect(disp, B_BLUE, [x[0], x[1], GRID_SIZE, GRID_SIZE])
        #snake = pygame.draw.rect(disp, B_BLUE, [start_x, start_y, GRID_SIZE, GRID_SIZE])

def background(disp):   ## -----This function will help create our screen 600x600 and initiate the game
    pygame.init()

    #Create a background big enough for the snake to move around
    disp = pygame.display.set_mode((WIDTH, HEIGHT))
    print('******')
    print(disp)
    pygame.display.update() #utilize to update changes made on the game.
    pygame.display.set_caption("Snake Game by Gi Diaz") #This will display the name on the heading

    return disp



def intro_fill(disp):   ## ----Creating an Intro window that will then open the main
    pygame.init()
    disp = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()
    pygame.display.set_caption("Welcome to the Snake Game")

    return disp





## --------------------------------Unused functions created for other or same purposes and to compare.
    # font = pygame.font.SysFont(None, 20)  ## FONT_STYLE = pygame.font.SysFont("arial", 40)
    #                                     ## SysFont(name, size, bold=False, italic=False) -> Font
    # text = font.render('You Lose', True, B_WHITE)
    # disp.blit(text, [WIDTH/6, HEIGHT/3])
    # pygame.display.update()
    # time.sleep(2)

        #creating a grid for coordinates
        # def_grid(disp, GRID_SIZE)
        # if start_x >= WIDTH or start_x < 0 or start_x >= HEIGHT or start_y < 0:
        #     game_over = True
    #creating a grid for coordinates
        # def_grid(disp, GRID_SIZE)
        # if start_x >= WIDTH or start_x < 0 or start_x >= HEIGHT or start_y < 0:
        #     game_over = True
# def make_canvas(width, height, title=None):
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()

    return canvas


    # canvas = make_canvas(WIDTH, HEIGHT, "You Lost")
    # canvas.create_text(20, 200, anchor='w', font='Courier 30', text='If you would like to quit, Press Q.')
    # canvas.mainloop()

# def def_grid(disp, GRID_SIZE):
    # for x in range(0, WIDTH, GRID_SIZE):
    #         for y in range(0, HEIGHT, GRID_SIZE):
    #             square = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
    #             pygame.draw.rect(disp, B_WHITE, square, 1) 
    

    #creating a grid for coordinates
        # def_grid(disp, GRID_SIZE)


        # if start_x >= WIDTH or start_x < 0 or start_x >= HEIGHT or start_y < 0:
        #     game_over = True

if __name__ == "__main__":
    main()