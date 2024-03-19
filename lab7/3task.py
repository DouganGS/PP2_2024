import pygame

pygame.init()
size = width,height = 500,500
screen = pygame.display.set_mode((size))
black = 0,0,0
red = 255,0,0
x = width/2
y = height/2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y >= 60:
                    y -= 20
            elif event.key == pygame.K_DOWN:
                if y <= height-60:
                    y += 20
            elif event.key == pygame.K_LEFT:
                if x >= 60:
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x <= width -60:
                    x += 20
            #ball cant move through screen line
    screen.fill((black))
    pygame.draw.circle(screen,(red),(x,y),50)
    
    pygame.display.flip()