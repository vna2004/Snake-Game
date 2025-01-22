import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (41, 240, 26)
red = (201, 18, 18)
yellow = (239, 250, 32)

win_width = 700
win_height = 500

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
#time.sleep(5)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

#fonts = pygame.font.get_fonts()
#print(fonts)
font_style = pygame.font.SysFont("consolas", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


def user_score(score):
    number = score_font.render("Score :"+str(score), True, yellow)
    window.blit(number, [0,0]) #to display with coordinates
    
def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])
        

def message(msg, color):
    msg = font_style.render(msg, True, color)
    window.blit(msg, [0, win_height/2])

def game_loop():
    gameOver = False
    gameClose = False
    
    x1 = win_width/2
    y1 = win_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_length_list = []
    snake_length = 1 #initial snake length
    
    foodx = round(random.randrange(0, win_width -snake)/10.0)*10.0
    foody = round(random.randrange(0, win_height - snake)/10.0)*10.0
    
    while not gameOver :
        
        while gameClose == True:
            window.fill(white)
            message("You Lost!! press P to Play again and Q to Quit the Game.", red)
            user_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:
                        game_loop()
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake
                        y1_change = 0
                    if event.key == pygame.K_RIGHT:
                        x1_change = snake
                        y1_change = 0
                    if event.key == pygame.K_UP:
                        x1_change = 0
                        y1_change = -snake
                    if event.key == pygame.K_DOWN:
                        x1_change = 0
                        y1_change = snake
                    
            if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
                gameClose = True
            x1 += x1_change
            y1 += y1_change
            window.fill(black)
            
            pygame.draw.rect(window, red, [foodx, foody, snake, snake])
            snake_size =[]
            snake_size.append(x1)
            snake_size.append(y1)
            snake_length_list.append(snake_size)
            if len(snake_length_list) > snake_length:
                del snake_length_list[0]
                
            game_snake(snake, snake_length_list)
            user_score(snake_length - 1)
            
            pygame.display.update()
            
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, win_width -snake)/10.0)*10.0
                foody = round(random.randrange(0, win_height - snake)/10.0)*10.0
                snake_length +=1
            
            clock.tick(snake_speed)
                
    pygame.quit()
    quit()
    
game_loop()            
                
                        
                    
            
