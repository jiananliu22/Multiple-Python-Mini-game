import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((400,400))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay) # 把整个gameDisplay赋给pixAr
pixAr[10, 20] = white
# pixAr[10][20] = white # it's OK, too

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
