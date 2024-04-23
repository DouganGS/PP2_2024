import pygame as py
from random import randint

py.init()

W,H= 596,671
screen = py.display.set_mode((W,H),py.RESIZABLE)

#background
bg = py.image.load(r'lab8\racer\bg.png').convert_alpha()
bg_y = 0
#player
player = py.image.load(r'lab8\racer\player.png').convert_alpha() # 90 160
player_x = 350
player_y = 500
#coin
coin = py.image.load(r'lab8\racer\coin.png').convert_alpha()
coins = []
coin_interval = 125
spawn_timer = coin_interval
coins_collection = 0
#text
myfont = py.font.Font(r'lab8\racer\r.ttf',40)
#fps
gameplay = True
clock = py.time.Clock() 
while True:
    if gameplay:
        #background
        screen.blit(bg,(0,bg_y))
        screen.blit(bg,(0,bg_y-H))
        
        #player
        screen.blit(player,(player_x,player_y))
        player_rect = player.get_rect(topleft=(player_x,player_y))
        
        #moving
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            player_x -= 10
        elif keys[py.K_RIGHT]:
            player_x += 10
        if keys[py.K_LEFT] and player_x < 121: #463
            gameplay = False
        elif keys[py.K_RIGHT] and player_x > 463-player.get_width():
            gameplay = False
        
        if keys[py.K_UP] and player_y  > 0:
            player_y -= 10    
        elif keys[py.K_DOWN] and player_y < H-160:
            player_y += 10
        
        #coin spawn
        spawn_timer -= 1
        if spawn_timer <= 0:
            coin_x = randint(121, 463 - coin.get_width())
            coin_y = randint(100, 300)
            coins.append(coin.get_rect(topleft=(coin_x,coin_y)))
            spawn_timer = coin_interval
        for coin_rect in coins:
            screen.blit(coin,coin_rect)
            coin_rect.y += 3
            if coin_rect.y >= 671:
                coins.remove(coin_rect)
            elif player_rect.colliderect(coin_rect):
                coins_collection += 1
                coins.remove(coin_rect) 
        
        #n-th coins
        text_surface = myfont.render(f'Your current coins: {coins_collection}',False,"Red")
        screen.blit(text_surface,(80,10))
        
        #move background    
        bg_y +=3
        if bg_y >= 672:
            bg_y = 0
    else:
        screen.fill("Gray")
        text_surface = myfont.render(f'Game Over', False, "Red")
        screen.blit(text_surface, (200, 300)) 
            
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    clock.tick(30)
