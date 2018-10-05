import pygame


pygame.init()


display_width = 1000
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
yellow = (127,255,170)
x_change = 0
y_change = 0

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar_trans.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45) 
y = (display_height * 0.75) 



def xchange():
    global x_change, x, y_change, y
    x = (x + x_change) % display_width
    y = (y + y_change) % display_height

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    #press key
    if event.type == pygame.KEYDOWN:
    	if event.key == pygame.K_LEFT:
    	    x_change = -5
    	elif event.key == pygame.K_RIGHT:
    	    x_change = 5
    	elif event.key == pygame.K_UP:
    	    y_change = -5
    	elif event.key == pygame.K_DOWN:
    	    y_change = 5        
        	
    	    	
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0 
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:   
            y_change = 0
    
    xchange()

    gameDisplay.fill(yellow)
    car(x,y)


        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
