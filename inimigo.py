# trabalhando com sprite no pygame
import pygame as pg
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random  
enemy_list = []

class Inimigo(pg.sprite.Sprite):
    """  Define aqui o construtor e outros metodos  """
    def __init__(self, width, height):
        super(Inimigo,self).__init__() # chama o construtor pai
        self.width = width
        self.height = height
        self.surf = pg.Surface((50,50))
        self.surf.fill((255,128,70))
        self.rect = self.surf.get_rect(
            center = (200, 200)
        )
        self.speed = 3
        self.sentido = "d"
        

    """
    def create_enemy(self):
        x = 50
        y = 25
        dist = 10
        enemy = pg.rect(x, y, self.width, self.height)
        enemy_list.append(enemy)
        x = x + dist
    """
    
    def limite(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.sentido = "d"
        if self.rect.right > self.width:
            self.rect.right = self.width
            self.sentido = "e"

    
    def update(self):
        if self.sentido == "d":
            self.rect.move_ip(self.speed, 0)
        if self.sentido == "e":
            self.rect.move_ip(-self.speed, 0)
        self.limite()
    
        
        
        