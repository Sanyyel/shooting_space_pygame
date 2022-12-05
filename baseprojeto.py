import pygame as pg
import pygame_menu
from pygame_menu import themes
import pygame.freetype
import tiro
import player
import inimigo
import random
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.locals import (
    K_SPACE, K_ESCAPE, KEYDOWN, QUIT
)



#adicionaEnemy = pg.USEREVENT + 1


largura = 400
altura = 400

preto = (0,0,0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

######################################################################
pg.mixer.init()
pg.init()

som_colisao = pg.mixer.Sound("explosao.wav")

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Projeto final DS404 21420 21723")
######################################################################

#pg.time.set_timer(adicionaEnemy, 1000)

# inicializar jogador
nave_player = pg.image.load("nave.png")
nave_player = pg.transform.scale(nave_player, (50, 25))
jogador = player.Player(largura, altura)

# inicializar inimigos
enemy_png = pg.image.load("enemy.png")
enemy_png = pg.transform.scale(enemy_png, (25, 25))
inimigos_linha1 = pg.sprite.Group()

i = 0
for i in range (8):
    enemy = inimigo.Inimigo(largura, altura)
    inimigos_linha1.add(enemy)

inimigos_linha2 = pg.sprite.Group()
i = 0
for i in range (8):
    enemy = inimigo.Inimigo(largura, altura)
    inimigos_linha2.add(enemy)

inimigos_linha3 = pg.sprite.Group()
i = 0
for i in range (8):
    enemy = inimigo.Inimigo(largura, altura)
    inimigos_linha3.add(enemy)

# inicializar tiros
tiros = pg.sprite.Group()

# fps clock
clock = pg.time.Clock()

def comecar():
    running = True
    while running:
        clock.tick(30)
        tela.fill(preto)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    tr = tiro.Tiro(
                        jogador.rect.centerx,
                        jogador.rect.centery
                    )
                    tiros.add(tr)

        
        game_over = False

        teclas = pg.key.get_pressed()
        jogador.update(teclas)
        tela.blit(nave_player, jogador.rect)

        posx = 10
        posy = 10
        dist = 50
        for ini in inimigos_linha1:
            ini.update()
            tela.blit(enemy_png, (posx, posy))
            posx = posx + dist

        posx = 10
        posy = 100
        dist = 50
        for ini in inimigos_linha2:
            ini.update()
            tela.blit(enemy_png, (posx, posy))
            posx = posx + dist

        posx = 10
        posy = 200
        dist = 50
        for ini in inimigos_linha3:
            ini.update()
            tela.blit(enemy_png, (posx, posy))
            posx = posx + dist
        

        for tr1 in tiros:
            tr1.update()
            tela.blit(tr1.surf, tr1.rect)
            if pg.sprite.spritecollide(tr1, inimigos_linha1, dokill=True):
                som_colisao.play()
                tiros.remove(tr1)
                tr1.kill
        
        if not inimigos_linha1.has(ini):
            game_over = True
        
        if game_over:
            font = pg.font.Font('freesansbold.ttf', 32)
            text = font.render('Game Over', True, vermelho, azul)
            textRect = text.get_rect()
            textRect.center = (largura//2, altura//2)

        pg.display.flip()

    pg.mixer.quit()
    pg.quit()
#criando menu
menu_principal = pygame_menu.Menu("Shooting Space", 400, 400,
                                    theme=themes.THEME_BLUE)
menu_principal.add.button("Jogar", comecar)
menu_principal.add.button("Sair", pygame_menu.events.EXIT)
menu_principal.mainloop(tela)

