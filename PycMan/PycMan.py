import pygame

pygame.init()


red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)

dis_width = 1000
dis_height = 1000

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("PycMan by artretr0")

clock = pygame.time.Clock()

pac_block = 10
game_speed = 30

font_style = pygame.font.SysFont(None, 40)

# Trying to create a menu
# will continue on this later.

"""
text = font_style.render('PycMan by artretr0 in development!', True, black, red)
text_rect = text.get_rect()
text_rect.center = (dis_width / 2, dis_height / 2)
"""

def game_loop():
    game_over = False
    game_close = False

    pac_posx = dis_width / 2
    pac_posy = dis_height / 2

    posx_change = 0
    posy_change = 0

    while not game_over:
        dis.fill(black)
        #dis.blit(text, text_rect) menu for the future
        pygame.draw.circle(dis, yellow, [pac_posx, pac_posy], 10)
        pygame.display.update()
        
        #Faz o jogo fechar quando o user clicar no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            #Movimentação do PacMan
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx_change = -pac_block
                    posy_change = 0
                elif event.key == pygame.K_RIGHT:
                    posx_change = pac_block
                    posy_change = 0
                elif event.key == pygame.K_UP:
                    posx_change = 0
                    posy_change = -pac_block
                elif event.key == pygame.K_DOWN:
                    posx_change = 0
                    posy_change = pac_block
                elif event.key == pygame.K_a:
                    posx_change = -pac_block
                    posy_change = 0
                elif event.key == pygame.K_d:
                    posx_change = pac_block
                    posy_change = 0
                elif event.key == pygame.K_w:
                    posx_change = 0
                    posy_change = -pac_block
                elif event.key == pygame.K_s:
                    posx_change = 0
                    posy_change = pac_block
            
        #Delimitando as paredes -> Se bater ele volta
        #Se for para a direita
        if pac_posx >= dis_width:
            posx_change = -pac_block
        #Se for para a esquerda
        if pac_posx < 0:
            posx_change = +pac_block
        #Se for para baixo
        if pac_posy >= dis_height:
            posy_change = -pac_block
        #Se for para cima
        if pac_posy < 0:
            posy_change = +pac_block

        pac_posx += posx_change
        pac_posy += posy_change
    
        pygame.display.update()
        clock.tick(game_speed)

    pygame.quit()
    quit()

game_loop()