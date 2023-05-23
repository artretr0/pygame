import pygame
#import time
import random

pygame.init()

dis_height = 1000
dis_width = 1000
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Trying to learn Python W/ Snake Game by artretr0")

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

snake_block = 10

clock = pygame.time.Clock()
snake_speed = 20

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/5, dis_height/3])

def snake_size(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def score_dis(score):
    value = score_font.render("Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

def game_loop():

    x1, y1 = dis_width/2 , dis_height/2
    x1_change, y1_change = 0, 0
    snake_list = []
    lenght_snake = 1

    game_over = False
    game_close = False

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Game Over! Press Q-Quit or C-Continue", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
         
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close == True

        snake_size(snake_block, snake_list)    
        score_dis(lenght_snake - 1)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            lenght_snake += 1

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()