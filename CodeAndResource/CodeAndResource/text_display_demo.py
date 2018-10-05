import pygame
import time
import random

pygame.init()



display_width = 800
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (175,238,238)
blue = (30,144,255)
bright_blue = (0,191,255)
pink = (255,20,147)
pause = False
car_width = 90

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar_trans_small.png')
carImg_crash = pygame.image.load('racecar_crash_trans_small.png')
gameIcon = pygame.image.load('myIcon.png')
edge_left = pygame.image.load('edge_left.png')
edge_right = pygame.image.load('edge_right.png')
carImg_move = pygame.image.load('racecar_trans_small_move.png')

pygame.display.set_icon(gameIcon)

def quit_game():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False    

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def car_move(x,y):
    gameDisplay.blit(carImg_move,(x,y))
    pygame.display.update()
            

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #global crashed
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_intro()
    
    

def crash(x,y,score):
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(green)
        gameDisplay.blit(carImg_crash,(x,y))        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("You crashed!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        score_font = pygame.font.SysFont("comicsansms",75)
        score_text = score_font.render('score:'+str(score), True, red)
        gameDisplay.blit(score_text, [310, 180])

        button("Go again!",150, 100, 100, 50, blue, bright_blue,game_loop)
        button("Quit",550, 100, 100, 50, blue, bright_blue, quit_game)

        pygame.display.update()
        clock.tick(20)     
    #message_display('You Crashed')

## button
def button(msg, x, y, w, h, in_color, ac_color, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() # return [1,0,0] or [1,0,1] or [0,1,0] depending on which mouse_pos is clicked
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac_color,(x,y,w,h))
        if click[0] == 1: #and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, in_color,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)    
## pause function

def paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150, 500, 100, 50, blue, bright_blue,unpause)
        button("Quit",550, 500, 100, 50, blue, bright_blue, quit_game)

        pygame.display.update()
        clock.tick(20)      
    


## intro 
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(green)
        intro_font = pygame.font.SysFont("comicsansms",115)
        intro_text = intro_font.render('A bit Racey', True, black)
        gameDisplay.blit(intro_text, [125, 280])

        button("Go!", 150, 500, 100, 50, blue, bright_blue, game_loop)
        button("Quit", 550, 500, 100, 50, blue, bright_blue, quit_game)

        pygame.display.update()
        clock.tick(20)

                    
    
def game_loop():
    global pause

    pygame.mixer.music.load('guiji_jaychou.mp3')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height - 100)

    x_change = 0
    score = 0

    #init thing function
    counter = (score + 10) // 10
    thing_x = []
    for i in range (counter):
        thing_startx = random.randrange(0, display_width)
        thing_x.append(thing_startx)
    ########
    thingx_speed_group = []
    thingx_speed = 0 
    for i in range (counter):
        thingx_speed_group.append(thingx_speed)    
    ########
    thing_starty = 0
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    thing_color = random.choice([black, white, red, blue, pink])
    ##

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #gameExit = True the reason why we do not use it:When you crash, you don't exit current game_loop, but start a new one 
                #while being still inside. So when you quit the new one, you return to
                 #the one where  you have already crashed, showing "You Crashed" message 
                #and starting all over again.﻿ the new one means the display页面 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 - (score // 10) * 1.2
                    car_move(x,y)
                if event.key == pygame.K_RIGHT:
                    x_change = 5 + (score // 10) * 1.2
                    car_move(x,y)
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(green)
        car(x,y)
        gameDisplay.blit(edge_left,(0,display_height - 102))
        gameDisplay.blit(edge_right,(display_width - 117,display_height - 102))

        ##score
        score_font = pygame.font.SysFont("comicsansms",25)
        score_text = score_font.render('score:'+str(score), True, red)
        gameDisplay.blit(score_text, [650, 50])
        ##

        ## use function of rect and uodate its position
        
        for thing_startx in thing_x: 
            #thing_startx = random.randrange(0, display_width)
            things(thing_startx, thing_starty, thing_width, thing_height, thing_color)
        thing_starty += thing_speed
        ##
        
        if x > display_width - car_width or x < 0:
            crash(x,y,score)

        #really crash
        if y <= thing_starty+thing_height:
            for thing_startx in thing_x: 
                if thing_startx <= x and x <= thing_startx + thing_width or  thing_startx <= x + car_width and x + car_width <= thing_startx + thing_width or x <= thing_startx and x + car_width >= thing_startx + thing_width:
                    crash(x,y,score) 

        # keep rect in the screen
        if thing_starty >= display_height:
            score += 1
            thing_starty = -thing_height
            if score % 10 == 0:
                thing_speed += 0.3
            counter = (score + 10) // 10
            thing_x = []
            level = min (counter, 3)
            for i in range (level):
                thing_startx = random.randrange(0, display_width)
                thing_x.append(thing_startx)
            thing_color = random.choice([black, white, red, blue, pink])
            ##
            

        
        
        pygame.display.update()
        clock.tick(70)

game_intro()
game_loop()
pygame.quit()
quit()
