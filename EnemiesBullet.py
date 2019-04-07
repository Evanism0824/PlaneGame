import pygame
from Tool import *
class EnemiesBullet(pygame.sprite.Sprite):
    '''创建敌机炮弹类'''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemies_bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > 600:
            self.kill()
