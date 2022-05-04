from pygame import *
from random import *
score = 0
life = 3
font.init()
font2 = font.SysFont('Arial', 30)
font3 = font.SysFont('Arial', 70)
e1 = 3
e2 = 3
e3 = 3
e4 = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet1(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -41:
            self.kill()
class Bullet2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.kill()  
class Bullet3(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -41:
            self.kill()
class Bullet4(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width:
            self.kill()
class Player(sprite.Sprite):
    def __init__(self, px, py, player_speed):
        super().__init__()   
        self.wer = 'greenup.png'
        self.ger = 'up'
        self.image = transform.scale(image.load(self.wer), (60, 80))        
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.speed = player_speed
    def up(self):
        self.ger = 'up'
        self.wer = 'greenup.png'
        self.image = transform.scale(image.load(self.wer), (60, 80))
    def down(self):
        self.ger = 'down'
        self.wer = 'greendown.png'
        self.image = transform.scale(image.load(self.wer), (60, 80))
    def left(self):
        self.ger = 'left'
        self.wer = 'greenleft.png'
        self.image = transform.scale(image.load(self.wer), (80, 60))
    def right(self):
        self.ger = 'right'
        self.wer = 'greenright.png'
        self.image = transform.scale(image.load(self.wer), (80, 60))
    def update(self):
        keya = False
        keyd = False
        keyw = False
        keys = False
        keys_pressed = key.get_pressed()
        if keya == True:
            player.left()
        if keyw == True:
            player.up()
        if keyd == True:
            player.right()
        if keys == True:
            player.down()
        if keys_pressed[K_a] and self.rect.x > 5:
            player.left()
            self.rect.x -= self.speed
            keya = True
            keyd = False
            keyw = False
            keys = False        
        if keys_pressed[K_d] and self.rect.x < win_width - 75:           
            player.right()
            self.rect.x += self.speed
            keyd = True
            keya = False
            keyw = False
            keys = False
        if keys_pressed[K_w] and self.rect.y > 5:
            player.up()
            self.rect.y -= self.speed
            keyw = True
            keyd = False
            keya = False
            keys = False
        if keys_pressed[K_s] and self.rect.y < win_height - 75:
            player.down()
            self.rect.y += self.speed
            keys = True
            keyd = False
            keyw = False
            keya = False
    def fire(self):
        keys_pressed = key.get_pressed()
        if self.ger == 'left':
            bullet3 = Bullet3('bulletleft.png', self.rect.centerx, self.rect.centery - 21, 42, 26, 10)
            bullets.add(bullet3)
        if self.ger == 'right':
            bullet4 = Bullet4('bulletright.png', self.rect.centerx, self.rect.centery - 21, 42, 26, 10)
            bullets.add(bullet4)     
        if self.ger == 'up':
            bullet1 = Bullet1('bulletup.png', self.rect.centerx - 13, self.rect.centery, 26, 42, 10)
            bullets.add(bullet1)
        if self.ger == 'down':
            bullet2 = Bullet2('bulletdown.png', self.rect.centerx - 13, self.rect.centery, 26, 42, 10)
            bullets.add(bullet2)  
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global life
        if self.rect.y > win_height:
            self.rect.x = randint(60, win_width - 60)
            self.rect.y = randint(-460, -80)
class Enemy2(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        global life
        if self.rect.y < -80:
            self.rect.x = randint(60, win_width - 60)
            self.rect.y = randint(win_height + 80, win_height + 460)
class Enemy3(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global life
        if self.rect.x > win_width:
            self.rect.y = randint(60, win_height - 60)
            self.rect.x = randint(-460, -80)
class Enemy4(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global life
        if self.rect.x < -80:
            self.rect.y = randint(60, win_height - 60)
            self.rect.x = randint(win_width + 80, win_width + 460)
class Asteroid1(GameSprite):
    def update(self):
        global e1
        self.rect.y += self.speed
        global life
        if self.rect.y > win_height:
            e1 = 3 
            self.rect.x = randint(60, win_width - 60)
            self.rect.y = randint(-460, -80)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Asteroid2(GameSprite):
    def update(self):
        global e2
        self.rect.y -= self.speed
        global life
        if self.rect.y < -80:
            e2 = 3
            self.rect.x = randint(60, win_width - 60)
            self.rect.y = randint(win_height + 80, win_height + 460)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Asteroid3(GameSprite):
    def update(self):
        global e3
        self.rect.x += self.speed
        global life
        if self.rect.x > win_width:
            e3 = 3 
            self.rect.y = randint(60, win_height - 60)
            self.rect.x = randint(-460, -80)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Asteroid4(GameSprite):
    def update(self):
        global e4
        self.rect.x -= self.speed
        global life
        if self.rect.x < -80:
            e4 = 3 
            self.rect.y = randint(60, win_height - 60)
            self.rect.x = randint(win_width + 80, win_width + 460)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_width = 1100
win_height = 700
bullets = sprite.Group()
window = display.set_mode((win_width, win_height))
display.set_caption('Shooter')
background = transform.scale(image.load('background.png'), (win_width, win_height))
player = Player(280, 280, 3)
asteroid1 = Asteroid1('redown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 1)
asteroid2 = Asteroid2('redup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 1)
asteroid3 = Asteroid3('redright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 1)
asteroid4 = Asteroid4('redleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 1)
monsters1 = sprite.Group()
for l in range(1,4):
    monster1 = Enemy1('graydown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 2)
    monsters1.add(monster1)
monsters2 = sprite.Group()
for m in range(1,4):
    monster2 = Enemy2('grayup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 2)
    monsters2.add(monster2)
monsters3 = sprite.Group()
for n in range(1,4):
    monster3 = Enemy3('grayright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 2)
    monsters3.add(monster3)
monsters4 = sprite.Group()
for o in range(1,4):
    monster4 = Enemy4('grayleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 2)
    monsters4.add(monster4)
finish = True
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                player.fire()
    if finish:
        window.blit(background, (0, 0))
        text = font2.render('СЧЕТ: ' + str(score), 1, (255, 255, 255))
        text_lose = font2.render('ЖИЗНИ: ' + str(life), 1, (255, 255, 255))
        hil = font3.render('ИГРА ОКОНЧЕНА', 1, (255, 255, 255))
        window.blit(text, (10, 10))
        window.blit(text_lose, (10, 40)) 
        collides = sprite.groupcollide(monsters1, bullets, True, True)
        collides2 = sprite.groupcollide(monsters2, bullets, True, True)
        collides3 = sprite.groupcollide(monsters3, bullets, True, True)
        collides4 = sprite.groupcollide(monsters4, bullets, True, True)
        for a in collides:
            score = score + 1
            monster1 = Enemy1('graydown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 2)
            monsters1.add(monster1)
        for b in collides2:
            score = score + 1
            monster2 = Enemy2('grayup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 2)
            monsters2.add(monster2)
        for c in collides3:
            score = score + 1
            monster3 = Enemy3('grayright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 2)
            monsters3.add(monster3)
        for d in collides4:
            score = score + 1
            monster4 = Enemy4('grayleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 2)
            monsters4.add(monster4)
        bullets.update()    
        bullets.draw(window)         
        monsters1.draw(window)
        monsters2.draw(window)
        monsters3.draw(window)
        monsters4.draw(window)
        asteroid1.reset()
        asteroid2.reset()
        asteroid3.reset()
        asteroid4.reset()
        player.update()
        player.reset()
        if life <= 0:
            window.blit(hil, (win_width / 2 - 280, win_height / 2 - 50))
            finish = False
        collider = sprite.spritecollide(player, monsters1, True)
        collider2 = sprite.spritecollide(player, monsters2, True)
        collider3 = sprite.spritecollide(player, monsters3, True)
        collider4 = sprite.spritecollide(player, monsters4, True)
        for e in collider:
            life = life - 1
            monster1 = Enemy1('graydown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 2)
            monsters1.add(monster1) 
        for f in collider2:
            life = life - 1
            monster2 = Enemy2('grayup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 2)
            monsters2.add(monster2) 
        for g in collider3:
            life = life - 1 
            monster3 = Enemy3('grayright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 2)
            monsters3.add(monster3)
        for k in collider4:
            life = life - 1 
            monster4 = Enemy4('grayleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 2)
            monsters4.add(monster4)
        if sprite.collide_rect(player, asteroid1):
            life = life - 1 
            asteroid1.kill()
            asteroid1 = Asteroid1('redown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 1)
            e1 = 3 
        if sprite.collide_rect(player, asteroid2):
            life = life - 1 
            asteroid2.kill()
            asteroid2 = Asteroid2('redup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 1)
            e2 = 3 
        if sprite.collide_rect(player, asteroid3):
            life = life - 1 
            asteroid3.kill()
            asteroid3 = Asteroid3('redright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 1)
            e3 = 3 
        if sprite.collide_rect(player, asteroid4):
            life = life - 1 
            asteroid4.kill()
            asteroid4 = Asteroid4('redleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 1)
            e4 = 3 
        if life > 3:
            life = 3
        if e1 <= 0:
            asteroid1.kill()
            asteroid1 = Asteroid1('redown.png', randint(60, win_width - 60), randint(-460, -80), 60, 80, 1)        
            e1 = 3 
            score = score + 1
            life = life + 1
        if e2 <= 0:
            asteroid2.kill()
            asteroid2 = Asteroid2('redup.png', randint(60, win_width - 60), randint(win_height + 80, win_height + 460), 60, 80, 1)
            e2 = 3 
            score = score + 1
            life = life + 1
        if e3 <= 0:
            asteroid3.kill()
            asteroid3 = Asteroid3('redright.png', randint(-460, -80), randint(60, win_height - 60), 80, 60, 1)
            e3 = 3 
            score = score + 1
            life = life + 1
        if e4 <= 0:
            asteroid4.kill()
            asteroid4 = Asteroid4('redleft.png', randint(win_width + 80, win_width + 460), randint(60, win_height - 60), 80, 60, 1)
            e4 = 3   
            score = score + 1
            life = life + 1
        collidet = sprite.spritecollide(asteroid1, bullets, True)
        collidet2 = sprite.spritecollide(asteroid2, bullets, True)
        collidet3 = sprite.spritecollide(asteroid3, bullets, True)
        collidet4 = sprite.spritecollide(asteroid4, bullets, True)
        for p in collidet:
            e1 = e1 - 1
        for q in collidet2:
            e2 = e2 - 1
        for r in collidet3: 
            e3 = e3 - 1
        for s in collidet4:
            e4 = e4 - 1
        monsters1.update() 
        monsters2.update()
        monsters3.update()  
        monsters4.update() 
        asteroid1.update() 
        asteroid2.update() 
        asteroid3.update() 
        asteroid4.update()            
        display.update()
    time.delay(15)