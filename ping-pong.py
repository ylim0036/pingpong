from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
#game scene:
back = (200, 255, 255) #background color (background) --- light blue? R, G, B
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(back)
    
#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60
    
#(self, player_image, player_x, player_y, player_speed, width, height)
#creating ball and paddles   
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)

# FONT IS OPTIONAL FOR TODAY    
font.init()
font = font.SysFont('Arial', 35) 

lose1 = font.render('PLAYER 1 - YOU LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 - YOU LOSE!', True, (180, 0, 0))
    
# ADD THIS AND TEST IT OUT!    
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.update_l()
    racket2.update_r()
    
    racket1.reset()
    racket2.reset()
    ball.reset()
    
    display.update()
    clock.tick(FPS)
