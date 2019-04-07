from pygame.locals import *
from Bullet import *
from Tool import *
from Missile import *
class Player(pygame.sprite.Sprite):
    '''创建玩家类'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(50, 38))
        # 设置图片表面颜色
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # 半径
        self.radius = 20
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10
        self.speedx = 0
        self.speedy = 0
        # 盾
        self.shield = 100
        # 设计延迟
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        # 设置初始声明
        self.lives = 5
        # 是否隐藏
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        # 火力
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH/2
            self.rect.bottom = HEIGHT-30
        self.speedx = 0
        self.speedy = 0
        #方向控制：A控制左、D控制右、W控制上、S控制下
        keystate = pygame.key.get_pressed()
        if keystate[K_a]:
            self.speedx = -5
        if keystate[K_d]:
            self.speedx = 5
        if keystate[K_w]:
            self.speedy = -5
        if keystate[K_s]:
            self.speedy = 5
        #发射控制：空格
        if keystate[pygame.K_SPACE]:
            self.shoot()
        #设置玩家移动边界
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 10:
            self.rect.top = 10
        if self.rect.bottom > HEIGHT-10:
            self.rect.bottom = HEIGHT-10
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self):
        now = pygame.time.get_ticks()
        if now-self.last_shot > self.shoot_delay:
            self.last_shot = now
            #单火力
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
            #双火力
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()
            #三火力
            if self.power >= 3:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                missile1 = Missile(self.rect.centerx, self.rect.top) # 导弹
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+200)

