import pygame
import random
import time
import datetime

pygame.init()
#music = pygame.mixer.music.load('themetune.mp3')
#pygame.mixer.music.play(-1)
#bullet_sound = pygame.mixer.Sound('gunshot.wav')


Times = (30,60,90,120,150,180,210,240,270,300)


waitTime = random.choice(Times)

black = (0,0,0)
grey = (65,61,68)
bright_grey =(85,81,88)
white = (255,255,255)

DisplayHeight = 600
DisplayWidth = 1000
FPS = 30
Clock = pygame.time.Clock()


win = pygame.display.set_mode((DisplayWidth,DisplayHeight))

icon = pygame.image.load('gun.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Shootout')
loadimg = pygame.image.load
#characters
background = loadimg('background.png')
Cowboy1 = loadimg('cowboy 1.png')

Cowboy1_shoot = loadimg('Cowboy 1 shooting.png') 
Cowboy1_shot = loadimg('Cowboy 1 shot.png')

Cowboy2 = loadimg('Cowbow2.png')
Cowboy2_shoot = loadimg('Cowboy2 (shooting).png')
Cowboy2_shot = loadimg('Cowboy 2 shot.png')

class players:
    def __init__(self,x,y,good):
        self.x = x
        self.y = y
        self.shot = False
        self.good = good
        self.shooting = False
        self.standing = True

    def draw (self, win):
        if self.good == True and self.standing == True:
            win.blit(Cowboy1,(self.x ,self.y ))
        elif self.good == True and self.shot == True:
            win.blit(Cowboy1_shot ,(self.x,self.y + 70))

        elif self.good == True and self.shooting == True:
            win.blit(Cowboy1_shoot,(self.x + 50,self.y -25))


        elif self.good == False and self.standing == True:
            win.blit(Cowboy2,(self.x,self.y))

        elif self.good == False and self.shot == True:
            win.blit(Cowboy2_shot ,(self.x,self.y + 80))

        elif self.good == False and self.shooting == True:
            win.blit(Cowboy2_shoot,(self.x +50,self.y + 50))





def draw_button(text,colour,bright_colour,x,y,length,width,action):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    

    if x + length > mouse[0] > x and y + width > mouse[1] > y:
        pygame.draw.rect(win,bright_colour,(x,y,length,width))

        if click[0] == 1:
            action()
            
            

            

    else:
        pygame.draw.rect(win,colour,(x,y,length,width))

    message_display_button(text,x+(length/2),y + (width/2),20)

    

def redrawGameWindow():
    win.blit(background,(0,0))
    Blue.draw(win)
    Red.draw(win)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf,TextRect = text_objects(text, largeText)
    TextRect.center = ((DisplayWidth/2), (DisplayHeight/2 -DisplayHeight/5))
    win.blit(TextSurf , TextRect)
    pygame.display.update()

def text_objects_button(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display_button(text,width,height,size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf,TextRect = text_objects_button(text, largeText)
    TextRect.center = ((width), (height))
    win.blit(TextSurf , TextRect)
    pygame.display.update()
        
        

Blue = players(100,425,True)
Red = players(700,400, False)

def game_intro():
    background = loadimg('background.png')

    
    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        

        win.blit(background,(0,0))
        message_display('Shoot Out')
        draw_button('Play',grey,bright_grey,DisplayWidth/2 - 50,DisplayHeight/2 + 100 ,150,50,game_loop)

        pygame.display.update()

def shot(team):

    end = True
    
    while end:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        message_display(team + 'Wins')
        draw_button('Replay',grey,bright_grey,DisplayWidth/2 - 100,DisplayHeight/2 + 100,150,50,game_loop)
        
    


def game_loop():

    Times = (30,60,90,120,150,180,210,240,270,300)

    waitTime = random.choice(Times)
    
    Blue.shooting = False
    Red.shot = False
    Red.shooting = False
    Blue.shot = False
    Red.standing = True
    Blue.standing = True

    run = True
    k = 1
    Go = 5
    
    while run:
        Clock.tick(FPS)
        redrawGameWindow()
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       
        if k == waitTime:
            
            if Go != 1:
                message_display('GO!')
            keys = pygame.key.get_pressed()    
            
            if keys[pygame.K_SPACE]:
                Blue.shooting = True
                Red.shot = True
                Red.shooting = False
                Blue.shot = False
                Red.standing = False
                Blue.standing = False
                Go = 1
                #bullet_sound.play()
                redrawGameWindow()
                shot('Blue')
                

            if keys[pygame.K_RETURN]:
                Red.shooting = True
                Blue.shot = True
                Blue.shooting = False
                Red.shot = False
                Red.standing = False
                Blue.standing = False
                Go = 1
                #bullet_sound.play()
                redrawGameWindow()
                shot('Red')
                
                
                
                
            
        else:
            k += 1

            redrawGameWindow()
        


 
game_intro()

pygame.quit()
quit
