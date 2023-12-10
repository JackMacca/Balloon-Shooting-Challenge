import pygame
import keyboard
import PlayerMovement
import Player

player = Player.Player()

class Ballon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        pygame.draw.circle(player.body, (123, 184, 44), (50, 300), 20, width=0)
        pygame.display.flip()


pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
ballon = Ballon()
run = True
screen.fill((255, 255, 255))
while run:
    screen.blit(player.body, player.rect, player.rect2)
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif keyboard.is_pressed('enter'):
                print("Enter Key")
                PlayerMovement.PlayerMovement.UpMovement()
        
# pygame.draw.circle()