import pygame
 
 
SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
FPS = 5 #Frames per second
 
overLap = pygame.image.load("data/overLap.png")

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('data/1.png'))
        self.images.append(pygame.image.load('data/2.png'))
        self.images.append(pygame.image.load('data/3.png'))
        self.images.append(pygame.image.load('data/4.png'))
        self.images.append(pygame.image.load('data/5.png'))
        self.images.append(pygame.image.load('data/6.png'))
        self.images.append(pygame.image.load('data/7.png'))
        self.images.append(pygame.image.load('data/8.png'))
        self.images.append(pygame.image.load('data/9.png'))
        self.images.append(pygame.image.load('data/10.png'))
        self.images.append(pygame.image.load('data/11.png'))
        self.images.append(pygame.image.load('data/12.png'))
        self.images.append(pygame.image.load('data/13.png'))
        self.images.append(pygame.image.load('data/14.png'))
        self.images.append(pygame.image.load('data/15.png'))
        self.images.append(pygame.image.load('data/16.png'))
        self.images.append(pygame.image.load('data/17.png'))

        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(0, 0, 150, 198)
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        my_group.draw(screen)
        screen.blit(overLap,(0,0))
        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()




