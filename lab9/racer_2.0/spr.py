import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, enemy_speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(topleft=(x, 0))
        self.enemy_speed = enemy_speed
        self.add(group)

    def update(self):
        self.rect.y += self.enemy_speed
        if self.rect.y >= 671:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x >= 121:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT] and self.rect.x <= 463-self.image.get_width():
            self.rect.x += 10
        
        if keys[pygame.K_UP]:
            self.rect.y -= 10    
        elif keys[pygame.K_DOWN]:
            self.rect.y += 10

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 3
        if self.rect.y >= 671:
            self.kill()
