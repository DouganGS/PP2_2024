import pygame
import time

pygame.init()
pygame.mixer.init()

musics = [r"lab7\barbie.wav",r"lab7\Hanging.wav"]
cur_track = 0
screen = pygame.display.set_mode((500,500))
image = pygame.image.load(r'lab7\radio.gif')
image_rect = image.get_rect()
pygame.mixer.music.load(musics[cur_track])
pygame.mixer.music.play()

def next_track():
    global cur_track
    cur_track = (cur_track+1) % len(musics)
    while cur_track == musics[cur_track]:
        cur_track = musics[cur_track]
    pygame.mixer.music.load(musics[cur_track])
    pygame.mixer.music.play()

def prev_track():
    global cur_track
    cur_track = (cur_track-1) % len(musics)
    pygame.mixer.music.load(musics[cur_track])
    pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                next_track()
            elif event.key == pygame.K_RIGHT:
                prev_track()
    screen.blit(image,image_rect)
    pygame.display.flip()

