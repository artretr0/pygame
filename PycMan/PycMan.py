import pygame

pygame.init()


red = (0, 0, 255)
black = (0, 0, 0)

dis_width = 1000
dis_height = 1000

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("PycMan by artretr0")

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/5, dis_height/3])

def game_loop():
    game_over = False
    game_close = False

    while not game_over:
            dis.fill(black)
            message("PycMan by artretr0 in development...", red)
            pygame.display.update()

    pygame.quit()
    quit()

game_loop()