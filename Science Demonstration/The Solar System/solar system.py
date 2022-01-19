'''
Author: Sourav
Date of Creation: 16/11/21
Class: 9th
Section: A
'''

#importing modules
import pygame
import math
import sys

pygame.init()

#screen variables
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

#variables
mainGame = True
fps =  30
clock = pygame.time.Clock()
images = {}

#colour variables
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (19,19,19)

#game images
images['icon'] = pygame.image.load("images/icon.png").convert_alpha()
images['bg'] = pygame.image.load("images/bg.png").convert_alpha()

images['mercury'] = pygame.image.load("images/mercury.png").convert_alpha()
images['venus'] = pygame.image.load("images/venus.png").convert_alpha()
images['earth'] = pygame.image.load("images/earth.png").convert_alpha()
images['mars'] = pygame.image.load("images/mars.png").convert_alpha()

#mercury object
class Mercury:

  def __init__(self):
    self.test = 0
    self.angle = 0
    self.image = images['mercury']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateMercury(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitMercury(self):
    self.angle += self.test
    mercuryRotated,mercuryRotatedRect = self.rotateMercury(self.image, self.angle)
    screen.blit(mercuryRotated,mercuryRotatedRect)

#venus object
class Venus:

  def __init__(self):
    self.test = 0
    self.angle = 0
    self.image = images['venus']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateVenus(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitVenus(self):
    self.angle += self.test
    venusRotated,venusRotatedRect = self.rotateVenus(self.image, self.angle)
    screen.blit(venusRotated,venusRotatedRect)

#earth object
class Earth:

  def __init__(self):
    self.test = 0
    self.angle = 0
    self.image = images['earth']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateEarth(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitEarth(self):
    self.angle += self.test
    earthRotated,earthRotatedRect = self.rotateEarth(self.image, self.angle)
    screen.blit(earthRotated,earthRotatedRect)

#mars object
class Mars:

  def __init__(self):
    self.test = 0
    self.angle = 0
    self.image = images['mars']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateMars(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitMars(self):
    self.angle += self.test
    marsRotated,marsRotatedRect = self.rotateMars(self.image, self.angle)
    screen.blit(marsRotated,marsRotatedRect)

#objects
earth = Earth()
mercury = Mercury()
venus = Venus()
mars = Mars()

mercuryRectImage = images['mercury'].get_rect(center = (mercury.positionX,mercury.positionY))
venusRectImage = images['venus'].get_rect(center = (venus.positionX,venus.positionY))
earthRectImage = images['earth'].get_rect(center = (earth.positionX,earth.positionY))
marsRectImage = images['mars'].get_rect(center = (earth.positionX,earth.positionY))

#defining icon and title
pygame.display.set_caption('Solar System')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['bg'],(0,0))
  
  mercury.blitMercury()
  venus.blitVenus()
  earth.blitEarth()
  mars.blitMars()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_p:

        mercury.test = 0
        venus.test = 0
        earth.test = 0
        mars.test = 0

      if event.key == pygame.K_s:

        mercury.test = 1.6074546675621
        venus.test = 1.175957018133
        earth.test = 1
        mars.test = 0.80849563465413

  clock.tick(fps)
  pygame.display.update()




