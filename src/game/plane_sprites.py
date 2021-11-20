import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹的事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_url, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_url)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    img_url = None

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 10)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机销毁 %s" % self.rect)


class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/me1.png")
        self.rect.bottom = SCREEN_RECT.bottom - 100
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

    def __del__(self):
        pass


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹销毁 %s" % self.rect)