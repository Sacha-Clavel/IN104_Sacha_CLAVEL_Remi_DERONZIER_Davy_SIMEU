import pygame
import random as rd
import  numpy as np
import time

# Taille matrice carte : 34x32


def main():

    pygame.init()
    running = True

    # Affichage divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("pacman.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pacman")

    # Creation de l'image Dot (Point pour mesurer la largeur des murs)

    Dot = pygame.image.load("Dot.png")

    # Largeur et hauteur de la fenêtre

    screen_width = 606
    screen_height = 715

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    Map_420px = pygame.image.load("map.png")
    Map = pygame.transform.scale(Map_420px,[screen_width,screen_height]) #Ajustement de l'image de fond
    screen.blit(Map, [0,0])
    pygame.display.set_mode((screen_width,screen_height))

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice Pacmans contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

    Pacman_Size=32

    Pacmans = []
    for i in range(0,360,90):
        Pacman_ligne = []
        for j in range(8):
            Pacman_1200px = pygame.image.load("pacman"+str(j)+".png")
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

    Seed_Px = pygame.image.load("seed.png")
    Seed = pygame.transform.scale(Seed_Px,[Seed_Size,Seed_Size])

    xseed = rd.randint(10,screen_width-10)
    yseed = rd.randint(10,screen_height-10)

    screen.blit(Seed,[xseed,yseed])

    # Premier affichage

    pygame.display.flip()

    # Paramètre de positons et de vitesse

    xpos = 50
    ypos = 50

    step = 3

    step_x = step
    step_y = 0

    epsilon = 15

    Score = 0

    Proportion = 7
    Longueur_queue = Proportion * step


    # Creation de la matrice représentant la carte et de la matrice des positions de chaque case matrice

    Nb_Pixels_Hauteur = screen_height
    Nb_Pixels_Largeur = screen_width

    Offset_x = 4
    Offset_y = 1

    Epaisseur_x = 27
    Epaisseur_y = 27
    Largeur = 23
    Hauteur = 27


    Mat_Map = [[0]*Largeur]*Hauteur
    Tab_Pos = [[[Offset_y + j*Epaisseur_x,Offset_x + i*Epaisseur_y] for i in range(Largeur)] for j in range(Hauteur)]

    font=pygame.font.Font(None, 40)
    #screen.blit(Mat_Map,[0,0])
    pygame.display.flip()



    while running:

        # Affichage du score de la partie

        font=pygame.font.Font(None, 19)
        text = font.render("Score = " + str(Score),1,(255,255,255))
        screen.blit(text, (screen_width/2-80, 10))


        j+=1

        j=j%8

        for event in pygame.event.get():

            # Condition de sortie

            if event.type == pygame.QUIT:
                running = False

            # Déplacements du pacman en fonction des entrées claviers

            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_a:
                    step_x = -step  # Exemple : on va vers la gauche si a est pressé
                    step_y = 0
                    i=2             # i=2 est la ligne de Pacmans correspondant à la tête de Pacman tournées à 180 degrés

                if event.key == pygame.K_d :
                    step_x = step
                    step_y = 0
                    i=0             # i=2 est la ligne de Pacmans correspondant à la tête de Pacman tournées à 0 degrés

                if event.key == pygame.K_w :
                    step_x = 0
                    step_y = -step
                    i=1             # i=2 est la ligne de Pacmans correspondant à la tête de Pacman tournées à 90 degrés

                if event.key == pygame.K_s :
                    step_x = 0
                    step_y = step
                    i=3

        Current_Pacman = Pacmans[i][j]

        # Si le pacman sort de l'écran, il boucle de l'autre côté

        if xpos>screen_width :
            xpos = -Pacman_Size

        if xpos < - Pacman_Size :
            xpos = screen_width

        if ypos>screen_height :
            ypos = -Pacman_Size

        if ypos< - Pacman_Size:
            ypos = screen_height

        # On actualise la position du pacman en fonction de la direction empruntée

        xpos += step_x
        ypos += step_y

        # On stocke dans Deplacements les valeurs de step_x,y du pacman
        # /!\ ???? méthode : a = np.vstack(truc,a) ???? /!\



        # Condition de mangeage de la graine par le pacman (condition de proximité)

        if abs(xpos+Pacman_Size/2 - (xseed+Seed_Size/2 )) <= epsilon and abs(ypos+Pacman_Size/2 - (yseed+Seed_Size/2) ) <= epsilon:

            Score += 1

            xseed = rd.randint(10,screen_width-10)
            yseed = rd.randint(10,screen_height-10)

        screen.blit(Seed,[xseed,yseed])


        screen.blit(Current_Pacman,(xpos, ypos))



        pygame.display.flip()
        screen.blit(Map, (0,0))
        Dot = pygame.transform.scale(Dot,[1,1])

        for i_Ligne in range(len(Mat_Map)) :

            for j_Colonne in range(len(Mat_Map[i_Ligne])) :

                y = Tab_Pos[i_Ligne][j_Colonne][0]
                x = Tab_Pos[i_Ligne][j_Colonne][1]

                text = font.render(str(Mat_Map[i_Ligne][j_Colonne]),1,(255,255,255))
                screen.blit(text, (x,y))
                screen.blit(Dot,(x,y))

        screen.blit(Dot,(182,190))




if __name__=="__main__":
    main()
