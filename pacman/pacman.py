import pygame
import random as rd
import numpy as np
import time

# Taille matrice carte : 27x23



def main() :

    pygame.init()
    running = True

    # Affichages divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("Images/pacman.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Images/Pacman")

    # Creation de l'image Dot (Point pour mesurer la largeur des murs)

    Dot = pygame.image.load("Images/Dot.png")

    # Largeur et hauteur de la fenêtre

    screen_width = 606
    screen_height = 715

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    Map_Px = pygame.image.load("Images/map.png")
    Map = pygame.transform.scale(Map_Px,[screen_width,screen_height]) #Ajustement de l'image de fond
    screen.blit(Map, [0,0])
    pygame.display.set_mode((screen_width,screen_height))

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice Pacmans contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

    Pacman_Size=32

    Pacmans = []
    for i in range(0,360,90):
        Pacman_ligne = []
        for j in range(8):
            Pacman_Px = pygame.image.load("Images/pacman"+str(j)+".png")
            Pacman = pygame.transform.scale(Pacman_Px,[Pacman_Size,Pacman_Size])
            Pacman_rotated = pygame.transform.rotate(Pacman,i)
            Pacman_ligne.append(Pacman_rotated)
        Pacmans.append(Pacman_ligne)

    i_Pacmans=0
    j_Pacmans=0

    # Initialisation des graines

    Seed_Size = 10

    Seed_Px = pygame.image.load("Images/seed.png")
    Seed = pygame.transform.scale(Seed_Px,[Seed_Size,Seed_Size])



    # Paramètre de positons et de vitesse

    xpos = 50
    ypos = 50

    step = 3

    step_x = step
    step_y = 0

    epsilon = 15

    Score = 0

    Mat_Map = [     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  ]



    # Creation de la matrice représentant la carte et de la matrice des positions de chaque case matrice

    Offset_x = 4
    Offset_y = 1

    Epaisseur_x = 27
    Epaisseur_y = 27
    Largeur = 23
    Hauteur = 27


    #Mat_Map = [[0]*Largeur]*Hauteur
    Tab_Pos = [[[Offset_y + j*Epaisseur_x,Offset_x + i*Epaisseur_y] for i in range(Largeur)] for j in range(Hauteur)]

    # Initialisation de l'affichage

    Pacman = Pacmans[i_Pacmans][j_Pacmans]
    screen.blit(Pacman,[xpos,ypos])

    screen.blit(Map, [0,0])

    for i in range(len(Mat_Map)) :

        for j in range(len(Mat_Map[i])) :

            if Mat_Map[i][j] == 1 :

                x_seed = Tab_Pos[i][j][1]
                y_seed = Tab_Pos[i][j][0]

                screen.blit(Seed, (x_seed,y_seed))



    pygame.display.flip()

    while running:

        for event in pygame.event.get():

            # Condition de sortie

            if event.type == pygame.QUIT:
                running = False



if __name__=="__main__":
    main()
