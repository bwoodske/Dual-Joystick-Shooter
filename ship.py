import pygame
import math

display_width = 1000
display_height = 800

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

class ship:
    def __init__(self, name):
        #Ship variables
        self.name = name
        self.xPos = display_width/2
        self.yPos = display_height/2
        self.xVelocity = 0
        self.yVelocity = 0

        self.spriteWidth = 25
        self.spriteHeight = 25

        #direction array = n,s,e,w
        self.direction = [0,0,0,0]

        #Bullet variables
        self.shotClock = 0
        self.bulletLocations = []
        self.bulletAngle = []
        self.bulletMovement = []
        self.bulletSpeed = 13

        #Sprites
        self.sprite = pygame.image.load('ship1.png')
        self.bullet = pygame.image.load('bullet.png')
        self.lastPos = self.sprite

    def move(self):
        self.xPos += self.xVelocity
        self.yPos += self.yVelocity

    def checkShot(self):
        if self.shotClock == 0:
            if pygame.mouse.get_pressed()[0] == 1:
                    self.shoot()

        if pygame.mouse.get_pressed()[0] == 0:
            self.shotClock = 0
        else:
            self.shotClock += 1
            if self.shotClock > 9:
                self.shotClock = 0


    def shoot(self):
        deltaY = (self.yPos - pygame.mouse.get_pos()[1])
        deltaX = (self.xPos - pygame.mouse.get_pos()[0])

        #Determining starting bullet location
        self.bulletLocations.append((self.xPos,self.yPos))

        #Determining bullet angle
        rads = math.atan2(-deltaY, deltaX)
        rads %= 2*math.pi
        angle = math.degrees(rads)
        if angle >= 270:
            angle -= 270
        else:
            angle += 90

        self.bulletAngle.append(angle)

        #Determining bullet trajectory
        angle = math.radians(angle) #Converts angle from degrees to radians

        xSpeed = math.sin(angle)*self.bulletSpeed
        ySpeed = math.cos(angle)*self.bulletSpeed

        self.bulletMovement.append((xSpeed,ySpeed))
        print(xSpeed, ySpeed)

    def moveBullets(self):
        toBeDeleted = []
        for x in range(0, len(self.bulletLocations)):
            a = list(self.bulletLocations[x])
            a[0] -= self.bulletMovement[x][0]
            a[1] -= self.bulletMovement[x][1]
            self.bulletLocations[x] = a
            # print(self.bulletLocations[x], a)

            #changing angle of bullet
            bullet = pygame.transform.rotate(self.bullet, self.bulletAngle[x])

            gameDisplay.blit(bullet, (a))

            #Detemining bullets that have hit a wall
            if self.bulletLocations[x][1] < 0 or self.bulletLocations[x][1] > display_height:
                toBeDeleted.append(x)

        for x in reversed(range(0,len(toBeDeleted))):
            del self.bulletLocations[toBeDeleted[x]]
            del self.bulletAngle[toBeDeleted[x]]
            del self.bulletMovement[toBeDeleted[x]]

    def draw(self):
        if self.direction[0] == 1 and self.direction[3] == 1:   #nw
            ship = pygame.transform.rotate(self.sprite, 45)
        elif self.direction[0] == 1 and self.direction[2] == 1: #ne
            ship = pygame.transform.rotate(self.sprite, 315)
        elif self.direction[1] == 1 and self.direction[2] == 1: #se
            ship = pygame.transform.rotate(self.sprite, 225)
        elif self.direction[1] == 1 and self.direction[3] == 1: #sw
            ship = pygame.transform.rotate(self.sprite, 135)
        elif self.direction[0] == 1:                            #n
            ship = self.sprite
        elif self.direction[1] == 1:                            #s
            ship = pygame.transform.rotate(self.sprite, 180)
        elif self.direction[2] == 1:                            #e
            ship = pygame.transform.rotate(self.sprite, 270)
        elif self.direction[3] == 1:                            #w
            ship = pygame.transform.rotate(self.sprite, 90)
        else:
            ship = self.lastPos

        self.lastPos = ship
        gameDisplay.blit(ship, (self.xPos, self.yPos))

    def update(self):
        self.moveBullets()
        self.move()
        self.draw()