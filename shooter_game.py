#Створи власний Шутер!

from models import *

display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), WINDOW_SIZE)

mixer.music.load('space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()

win = fontmassage.render("YOU WON!", 1, (0,255,0))
lose = fontmassage.render("YOU LOSE!",1, (255,0,0))

enemies = sprite.Group()
for i in range(5):
    enemies.add(Enemy('ufo.png', randint(0, WINDOW_SIZE[0]- SPSIZE[0]), randint(-250, SPSIZE[1]*(-1)), randint(1, 4), True  ))

asteroids = sprite.Group()
for i in range(3):
    asteroids.add(Enemy('asteroid.png', randint(0, WINDOW_SIZE[0]- SPSIZE[0]), randint(-250, SPSIZE[1]*(-1)), 1, False ))

player = Player('rocket.png', 250, WINDOW_SIZE[1]-SPSIZE[1], 10)

clock = time.Clock()
game_over = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not game_over:
        window.blit(background, (0,0))
        player.update_position()
        player.reset()
        player.fire()

        enemies.draw(window)
        enemies.update()

        asteroids.draw(window)
        asteroids.update()

        bullets.draw(window)
        bullets.update()

        for bullet in bullets:
            for enemy in enemies:
                if sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    enemy.kill()
                    counter.killed += 1
                    enemies.add(Enemy('ufo.png', randint(0, WINDOW_SIZE[0]- SPSIZE[0]), randint(-250, SPSIZE[1]*(-1)), randint(1, 4), True))
        sprite.groupcollide(bullets, asteroids, True, False)
        if sprite.spritecollide(player, enemies, False) or sprite.spritecollide(player, asteroids, False) or counter.lost >=3:
            window.blit(lose, (WINDOW_SIZE[0] / 2 , WINDOW_SIZE[1] / 2))
            game_over = True
        counter.show()
        if counter.killed >= 10:
            window.blit(win, (WINDOW_SIZE[0] / 2 , WINDOW_SIZE[1] / 2))
            game_over= True
        clock.tick(FPS)
        display.update()