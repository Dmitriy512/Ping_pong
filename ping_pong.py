from pygame import *

back_color = (200, 255, 255)
win_wigth = 600
win_height = 500
window = display.set_mode((win_wigth, win_height))
window.fill(back_color)

clock = time.Clock()
fps = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y -= self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y < 495:
            self.rect.y -= self.speed

racket1 = Player('', 20, 250, 2, 15, 100)
racket2 = Player('', 580, 250, 2, 15, 100)
ball = GameSprite('', 300, 250, 2, 50, 50)

font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == True:
        game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > win_wigth - 50 or ball.rect.x < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        
    if ball.rect.x > 600:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(fps)
