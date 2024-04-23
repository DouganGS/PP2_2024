import pygame
import random
from spr import Enemy, Player, Coin
pygame.init()

W, H = 596, 671
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Racer 2.0")

# images
bg = pygame.image.load(r'lab9\racer_2.0\images\bg.png').convert_alpha()
player_image = pygame.transform.scale(pygame.image.load(r'lab9\racer_2.0\images\player.png').convert_alpha(), (90, 160))
coin_image = pygame.image.load(r'lab9\racer_2.0\images\coin.png').convert_alpha()

# classes
player = Player(350, 500, player_image)
enemies_image = [r'lab9\racer_2.0\images\1.png', r'lab9\racer_2.0\images\2.png', r'lab9\racer_2.0\images\3.png']
enemies_surface = [pygame.transform.scale(pygame.image.load(enemy).convert_alpha(), (90, 160)) for enemy in enemies_image]
coin_interval = 125
spawn_timer = coin_interval
coins_collection = 0

# sprites
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

timer = pygame.time.set_timer(pygame.USEREVENT, 3000)
gameplay = True
bg_y = 0
clock = pygame.time.Clock() 
myfont = pygame.font.Font(r'lab9\racer_2.0\r.ttf',40)

def generate_enemy(group):
    indx = random.randint(0, len(enemies_surface) - 1)
    x = random.choice([150, 350])
    enemies_speed = random.randint(5, 10)
    return Enemy(x, enemies_speed, enemies_surface[indx], group)
def generate_coin():
    coin_x = random.randint(121, 463 - coin_image.get_width())
    coin_y = random.randint(100, 300)
    return Coin(coin_x, coin_y, coin_image)

while True: 
    if gameplay:
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - H))
        screen.blit(player.image, player.rect)
        player.update(gameplay)
        #coins
        spawn_timer -= 1
        if spawn_timer <= 0:
            coins.add(generate_coin())
            spawn_timer = coin_interval
        for coin_sprite in coins:
            coin_sprite.update()
            screen.blit(coin_sprite.image, coin_sprite.rect)
            if pygame.sprite.spritecollide(player, coins, True):
                coins_collection += random.randint(1, 5)
                for enemy_sprite in enemies:
                    enemy_sprite.enemy_speed += 0.09
                coin_sprite.kill()
        #current coins
        text_surface = myfont.render(f'Your current coins: {coins_collection}', False, "Red")
        screen.blit(text_surface, (80, 10))
        #background
        bg_y += 3
        if bg_y >= 672:
            bg_y = 0
        
        enemies.draw(screen)
        enemies.update()
    else:
        screen.fill("Gray")
        text_surface = myfont.render(f'Game Over', False, "Red")
        screen.blit(text_surface, (200, 300)) 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            generate_enemy(enemies)
        
    if pygame.sprite.spritecollide(player, enemies, False):
        gameplay = False
    clock.tick(30)
