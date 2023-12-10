import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.body = pygame.Surface([800, 600])
        self.body.fill((255,255,255))
        # body of gun
        pygame.draw.rect(self.body, (0, 0, 0), [670, 500, 80, 50])
        self.rect = self.body.get_rect()

        # shooter
        pygame.draw.rect(self.body, (0, 0, 0), [650, 515, 20, 20])
        self.rect2 = self.body.get_rect()