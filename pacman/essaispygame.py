import pygame
import random as rd

def main():

    pygame.init()
    running = True

    # Affichage divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/pacman.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pacman")

    # Largeur et hauteur de la fenêtre

    screen_width = 700
    screen_height = 700

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    Map_420px = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/map.png")
    Map = pygame.transform.scale(Map_420px,[screen_width,screen_height]) #Ajustement de l'image de fond
    screen.blit(Map, [0,0])

    # Initialisation du pacman et création des diverses formes de bouche du pacman

    Pacman_Size=35

    Pacmans = []
    for i in range(0,360,90):
        Pacman_ligne = []
        for j in range(8):
            Pacman_1200px = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/Pacman"+str(j)+".png")
            Pacman = pygame.transform.scale(Pacman_1200px,[Pacman_Size,Pacman_Size])
            Pacman_rotated = pygame.transform.rotate(Pacman,i)
            Pacman_ligne.append(Pacman_rotated)
        Pacmans.append(Pacman_ligne)

    i=0
    j=0

    xpos = 50
    ypos = 50

    screen.blit(Pacman,[xpos,ypos])

    # Initialisation des graines

    Seed_Size = 10

    Seed_Px = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/Seed.png")
    Seed = pygame.transform.scale(Seed_Px,[Seed_Size,Seed_Size+1])

    xseed = rd.randint(10,screen_width-10)
    yseed = rd.randint(10,screen_height-10)

    screen.blit(Seed,[xseed,yseed])

    # Premier affichage

    pygame.display.flip()

    # Paramètre de positons et de vitesse

    xpos = 50
    ypos = 50

    step = 6

    step_x = step
    step_y = 0

    epsilon = 15

    Score = 0

    while running:

        j+=1
        if j == 800:
            j=0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_a:
                    step_x = -step
                    step_y = 0
                    i=2

                if event.key == pygame.K_d :
                    step_x = step
                    step_y = 0
                    i=0

                if event.key == pygame.K_w :
                    step_x = 0
                    step_y = -step
                    i=1

                if event.key == pygame.K_s :
                    step_x = 0
                    step_y = step
                    i=3


        if xpos>screen_width :
            xpos = -Pacman_Size

        if xpos < - Pacman_Size :
            xpos = screen_width

        if ypos>screen_height :
            ypos = -Pacman_Size

        if ypos< - Pacman_Size:
            ypos = screen_height


        xpos += step_x
        ypos += step_y

        Current_Pacman = Pacmans[i][j%8]

        screen.blit(Current_Pacman, (xpos, ypos))

        font=pygame.font.Font(None, 40)
        text = font.render("Score = " + str(Score),1,(255,255,255))
        screen.blit(text, (screen_width/2-80, 10))

        pygame.display.flip()
        screen.blit(Map, (0,0))

        if abs(xpos+Pacman_Size/2 - (xseed+Seed_Size/2 )) <= epsilon and abs(ypos+Pacman_Size/2 - (yseed+Seed_Size/2) ) <= epsilon:
            xseed = rd.randint(10,screen_width-10)
            yseed = rd.randint(10,screen_height-10)
            Score += 1

        screen.blit(Seed,[xseed,yseed])




if __name__=="__main__":
    main()
