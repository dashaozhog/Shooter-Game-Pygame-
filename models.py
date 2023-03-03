from pygame import *
from random import randint
import time as my_time


WINDOW_SIZE = (700,500)
FPS = 60
SPSIZE = (65,65)
bullets = sprite.Group()
WHITE = (255,255,255)

window = display.set_mode(WINDOW_SIZE)
mixer.init()
fire_sound = mixer.Sound("fire.ogg")

font.init()
font_counter = font.Font(None, 24)
fontmassage = font.Font(None, 24)

interval = 0.5
firetime = 0

class Counter:
    def __init__(self, fontObj, color):
        self.lost = 0
        self.killed = 0
        self.fontObj = fontObj
        self.color = color
    def show(self):
        self.lostObj = self.fontObj.render("Пропущено: " +  str(self.lost), 1, self.color)
        window.blit(self.lostObj, (0,0))
        self.killedObj = self.fontObj.render("Вбито: " + str(self.killed), 1, self.color )
        window.blit(self.killedObj, (0,30))

counter = Counter(font_counter, WHITE)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), SPSIZE)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_position(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WINDOW_SIZE[0]-SPSIZE[0]:
            self.rect.x += self.speed

    def fire(self):
        # keys = key.get_pressed()
        # for ev in event.get():
        #     if ev.type == KEYDOWN:
        #         if ev.key == K_SPACE:
        #             key.set_repeat(1)
        #             fire_sound.play()
        #             bullet = Bullet("bullet.png", self.rect.x , self.rect.y, 5)
        #             bullets.add(bullet)
        global firetime
        keys = key.get_pressed()
        if keys[K_SPACE] and my_time.time()> firetime + interval:
            firetime = my_time.time()
            #fire_sound.play()
            bullet = Bullet("bullet.png", self.rect.x , self.rect.y, 5)
            bullets.add(bullet)



class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, is_destroy):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.is_destroy = is_destroy

    def update(self):
        if self.rect.y < WINDOW_SIZE[1]:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(0, WINDOW_SIZE[0]-SPSIZE[1])

            if self.is_destroy:
                counter.lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
    

