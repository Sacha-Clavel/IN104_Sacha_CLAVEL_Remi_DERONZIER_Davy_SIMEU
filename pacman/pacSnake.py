import pygame
import random as rd
import  numpy as np
import time

# Taille matrice carte : 34x32

def main():

    pygame.init()
    running = True

    # Affichage divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/pacman.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pacman")

    # Creation de l'image Dot (Point pour mesurer la largeur des murs)

    Dot = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/Dot.png")

    # Largeur et hauteur de la fenêtre

    screen_width = 600
    screen_height = 664

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    Map_420px = pygame.image.load("/Users/sachaclavel/Desktop/pacman_game/PacmanMap.png")
    Map = pygame.transform.scale(Map_420px,[screen_width,screen_height]) #Ajustement de l'image de fond
    screen.blit(Map, [0,0])

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice Pacmans contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

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

    Proportion = 10
    Longueur_queue = Proportion * step

    # Deplacements contiendra la suite des step_x,y qu'aura emprunté le pacman
    # Positions contiendra la liste des positions du pacman et des wagons

    Deplacements = np.zeros((Proportion,3))
    Positions = [[xpos,ypos]]

    # Creation de la matrice représentant la carte

    Mat_Map = np.zeros((34,32))


    while running:

        # Affichage du score de la partie

        font=pygame.font.Font(None, 40)
        text = font.render("Score = " + str(Score),1,(255,255,255))
        screen.blit(text, (screen_width/2-80, 10))


        j+=1

        if j == 80:
            j=0

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

        Current_Pacman = Pacmans[i][j%8]

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

        A = np.copy(Deplacements)
        Deplacements = np.vstack(([step_x,step_y,i],A))
        Deplacements = np.copy(Deplacements[:-1])

        # Condition de mangeage de la graine par le pacman (condition de proximité)

        if abs(xpos+Pacman_Size/2 - (xseed+Seed_Size/2 )) <= epsilon and abs(ypos+Pacman_Size/2 - (yseed+Seed_Size/2) ) <= epsilon:

            Score += 1

            # Si on a mangé une graîne, on a joute un wagon. La position initiale du wagon dépend de
            # la position du wagon précédent et de la direction de ce dernier.

            xfin = Positions[-1][0]
            yfin = Positions[-1][1]

            if Deplacements[-Proportion][0] <= 0 and  Deplacements[-Proportion][1] == 0:

                xfin += Longueur_queue

            if Deplacements[-Proportion][0] > 0 and  Deplacements[-Proportion][1] == 0 :

                xfin -= Longueur_queue

            if Deplacements[-Proportion][0] == 0 and  Deplacements[-Proportion][1] > 0 :

                yfin -= Longueur_queue

            if Deplacements[-Proportion][0] == 0 and  Deplacements[-Proportion][1] <= 0 :

                yfin += Longueur_queue

            Positions.append([xfin,yfin])

            A = np.copy(Deplacements)
            Deplacements=np.vstack((A,np.zeros((Proportion,3))))


            xseed = rd.randint(10,screen_width-10)
            yseed = rd.randint(10,screen_height-10)

        screen.blit(Seed,[xseed,yseed])

        for Index_Pos in range(len(Positions)) :

            if Index_Pos == 0:

                Positions[0] = [xpos,ypos]

                screen.blit(Current_Pacman,(xpos, ypos))

            else :


                k = Index_Pos*Proportion

                xposI = Positions[Index_Pos][0]
                yposI = Positions[Index_Pos][1]
                stepIx = Deplacements[k,0]
                stepIy = Deplacements[k,1]
                direction = int(Deplacements[k,2])
                Pacman_wagon_I = Pacmans[direction][j%8]

                xposI += stepIx
                yposI += stepIy

                Positions[Index_Pos] = [xposI, yposI]

                screen.blit(Pacman_wagon_I, [Positions[Index_Pos][0], Positions[Index_Pos][1]])

                if Positions[Index_Pos][0] > screen_width :
                    Positions[Index_Pos][0] = -Pacman_Size

                if Positions[Index_Pos][0] < - Pacman_Size :
                    Positions[Index_Pos][0] = screen_width

                if Positions[Index_Pos][1] > screen_height :
                    Positions[Index_Pos][1] = -Pacman_Size

                if Positions[Index_Pos][1] < - Pacman_Size:
                    Positions[Index_Pos][1] = screen_height

        pygame.display.flip()
        screen.blit(Map, (0,0))
        Dot = pygame.transform.scale(Dot,[1,1])
        screen.blit(Dot,(182,190))




if __name__=="__main__":
    main()
