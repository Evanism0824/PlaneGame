import random
from Tool import *
from EnemiesBullet import *
class Mob(pygame.sprite.Sprite):
    '''创建敌机类'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(enemies_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.90/2)
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(-150,-100)
        self.speedy = random.randrange(5,10)
        self.speedx = random.randrange(-3,3)
        self.shoot_delay = 1000
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if random.randrange(10) >= 6:
            self.enemies_shoot()
        if (self.rect.top > HEIGHT+10) or (self.rect.left < -25) or (self.rect.right > WIDTH+20):
            self.rect.x = random.randrange(0,WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

    def enemies_shoot(self):
        now = pygame.time.get_ticks()
        if now-self.last_shot > self.shoot_delay:
            self.last_shot = now
            enemies_bullet = EnemiesBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(enemies_bullet)
            enemies_bullets.add(enemies_bullet)
            shooting_sound.play()
