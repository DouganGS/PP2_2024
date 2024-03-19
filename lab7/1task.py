import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
FPS = 50
myClock = pygame.image.load(r'lab7\clocks.png')
myClock = pygame.transform.scale(myClock, (600, 600))


minute_arrow = pygame.image.load(r'lab7\right_hand.png') 
minute_arrow = pygame.transform.scale(minute_arrow, (20, 233))
second_arrow = pygame.image.load(r'lab7\left_hand.png')
second_arrow = pygame.transform.scale(second_arrow, (16, 266))


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        my_time = datetime.datetime.now()
        hourINT = int(my_time.strftime("%I"))
        minuteINT = int(my_time.strftime("%M"))
        secondINT = int(my_time.strftime("%S"))

        angleMINUTE = minuteINT * 6 * -1
        angleSECOND = secondINT * 6 * -1

        minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
        second = pygame.transform.rotate(second_arrow, angleSECOND)
        

        screen.fill((255, 255, 255))
        screen.blit(myClock, (100, 100))
        screen.blit(second, (399 - int(second.get_width() / 2), 400 - int(second.get_height() / 2)))
        screen.blit(minute, ((399 - int(minute.get_width() / 2), 400 - int(minute.get_height() / 2))))
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
        pygame.display.flip()
        clock.tick(FPS)