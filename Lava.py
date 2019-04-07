from Tool import *
import random
class Lava(pygame.sprite.Sprite):
    '''创建火山石类'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(lava_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.90/2)
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(-150,-100)
        self.speedy = random.randrange(5,10)
        self.speedx = random.randrange(-3,3)
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    #添加火山石旋转效果
    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now-self.last_update > 50:
            self.last_update = time_now
            self.rotation = (self.rotation+self.rotation_speed)%360
            new_image = pygame.transform.rotate(self.image_orig,self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > HEIGHT+10) or (self.rect.left < -25) or (self.rect.right > WIDTH+20):
            self.rect.x = random.randrange(0,WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
