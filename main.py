import pygame
from colours import *
from ship import *

pygame.init()

display_width = 1000
display_height = 800
FPS = 60

shipSpeed = 6

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("DJS")

gameExit = False

playerShip = ship("A name option will be added later")

while not gameExit:
    gameDisplay.fill(black)

    playerShip.checkShot()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameExit = True
        if event.type == pygame.KEYDOWN:
            #Ship Movement
            if event.key == pygame.K_w:
                playerShip.direction[0] = 1
                playerShip.direction[1] == 0
                playerShip.yVelocity = -shipSpeed
            elif event.key == pygame.K_s:
                playerShip.direction[1] = 1
                playerShip.direction[0] == 0
                playerShip.yVelocity = shipSpeed
            elif event.key == pygame.K_d:
                playerShip.direction[2] = 1
                playerShip.direction[3] == 0
                playerShip.xVelocity = shipSpeed
            elif event.key == pygame.K_a:
                playerShip.direction[3] = 1
                playerShip.direction[2] == 0
                playerShip.xVelocity = -shipSpeed


            elif event.key == pygame.K_p:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerShip.direction[0] = 0
                if playerShip.yVelocity == -shipSpeed:
                    playerShip.yVelocity = 0
            elif event.key == pygame.K_s:
                playerShip.direction[1] = 0
                if playerShip.yVelocity == shipSpeed:
                    playerShip.yVelocity = 0
            elif event.key == pygame.K_d:
                playerShip.direction[2] = 0
                if playerShip.xVelocity == shipSpeed:
                    playerShip.xVelocity = 0
            elif event.key == pygame.K_a:
                playerShip.direction[3] = 0
                if playerShip.xVelocity == -shipSpeed:
                  playerShip.xVelocity = 0

    playerShip.update()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()