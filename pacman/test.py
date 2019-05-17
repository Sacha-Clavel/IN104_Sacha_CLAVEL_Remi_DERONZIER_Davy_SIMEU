
import pygame
import random as rd
import utilities

# Taille matrice carte : 27x23


def main() :

    pygame.init()
    running = True

    # Affichages divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("images/pacman10.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pacman")

    # Creation de l'image Dot (Point pour mesurer la largeur des murs)

        #Dot = pygame.image.load("Images/Dot.png")

    # Largeur et hauteur de la fenêtre

    screen_width = 606
    screen_height = 775

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    map_org = pygame.image.load("images/map.png")
    map = pygame.transform.scale(map_org,[screen_width,screen_height]) #Ajustement de l'image de fond
    screen.blit(map, [0,0])

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice Pacmans contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

    pacman_size = 32



    pacmans = []

    for i in range(0,360,90):
        pacman_ligne = []

        for j in range(8):
            pacman_org = pygame.image.load("images/pacman"+str(j)+".png")
            pacman_rotated = pygame.transform.rotate(pacman_org,i)
            pacman = pygame.transform.scale(pacman_rotated,[pacman_size,pacman_size])
            pacman_ligne.append(pacman)
        pacmans.append(pacman_ligne)

    i_pacmans = 0
    j_pacmans = 0

    # Création des images graines

    seed_size = 10

    seed_px = pygame.image.load("Images/seed.png")
    seed = pygame.transform.scale(seed_px,[seed_size,seed_size])

# Creation des images des fantomes

    ghost_size = 30

    ghost_0_px = pygame.image.load("images/shadow.png")
    ghost_0 = pygame.transform.scale(ghost_0_px,[ghost_size,ghost_size])


    # Creation de la matrice représentant la carte et de la matrice des positions de chaque case matrice

    mat_map = [     [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
                    [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
                    [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
                    [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
                    [-1,  1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1,  1, -1],
                    [-1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [ 1,  1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1,  1,  1],
                    [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1],
                    [-1,  1,  1,  1,  1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1,  1,  1,  1, -1],
                    [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
                    [-1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1,  0,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1, -1],
                    [-1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1],
                    [-1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1],
                    [-1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1, -1],
                    [-1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1],
                    [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  ]


    offset_x = 1
    offset_y = 61

    pos_per_mvmt = 9
    step = 3
    epaisseur = step*pos_per_mvmt
    num_pos_pacman = 0
    num_pos_fantome_0 = 0

    largeur = 23
    hauteur = 27

    tab_pos = [[[offset_y + j*epaisseur,offset_x + i*epaisseur] for i in range(largeur)] for j in range(hauteur)]


    # Paramètre de positons et de vitesse

    liste_deplacements = ["rightward","upward","leftward","downward"]

    indice_pos_y_pacman = 20
    indice_pos_x_pacman = 11

    indice_pos_x_fantome_0 = 1
    indice_pos_y_fantome_0 = 1


    offset_pacman_x = 11
    offset_pacman_y = 11

    offset_fantome_0_x = 10
    offset_fantome_0_y = 10

    xpos_pacman = tab_pos[indice_pos_y_pacman][indice_pos_x_pacman][1] - offset_pacman_x
    ypos_pacman = tab_pos[indice_pos_y_pacman][indice_pos_x_pacman][0] - offset_pacman_y

    xpos_fantome_0 = tab_pos[indice_pos_y_fantome_0][indice_pos_x_fantome_0][1] - offset_fantome_0_x
    ypos_fantome_0 = tab_pos[indice_pos_y_fantome_0][indice_pos_x_fantome_0][0] - offset_fantome_0_y



    current_mvmt_pacman = "leftward"
    next_mvmt_choosed = True
    next_mvmt = "leftward"

    step_x_pacman = step
    step_y_pacman = 0
    step_x_pacman_mat = 1
    step_y_pacman_mat = 0


    current_mvmt_fantome_0 = liste_deplacements[0] # "rightward"

    step_x_fantome_0 = step
    step_y_fantome_0 = 0
    step_x_fantome_0_mat = 1
    step_y_fantome_0_mat = 0


    score = 0


    # Initialisation de l'affichage

    pacman = pacmans[i_pacmans][j_pacmans]

    screen.blit(map, [0,0])

    screen.blit(pacman,[xpos_pacman,ypos_pacman])


    for i in range(len(mat_map)) :

        for j in range(len(mat_map[i])) :

            if mat_map[i][j] == 1 :

                x_seed = tab_pos[i][j][1]
                y_seed = tab_pos[i][j][0]

                screen.blit(seed, (x_seed,y_seed))



    pygame.display.flip()

    while running:

        num_pos_fantome_0 += 1
        j_pacmans += 1
        j_pacmans = j_pacmans%8

        if next_mvmt_choosed :
            next_mvmt_choosed = False
            #next_mvmt = None

        else :

            next_mvmt = current_mvmt_pacman

            for event in pygame.event.get():

                # Condition de sortie

                if event.type == pygame.QUIT:
                    running = False

                    # Déplacements du pacman en fonction des entrées claviers

                if event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_LEFT:
                        next_mvmt = "leftward"

                    if event.key == pygame.K_RIGHT :
                        next_mvmt = "rightward"

                    if event.key == pygame.K_UP :
                        next_mvmt = "upward"

                    if event.key == pygame.K_DOWN :
                        next_mvmt = "downward"


        mvmt_charracteristics = utilities.mvmt_init(next_mvmt)
        step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
        step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
        step_x_pacman = step_x_pacman_mat * step
        step_y_pacman = step_y_pacman_mat * step
        i_pacmans = mvmt_charracteristics["i_pacmans"]


        next_indice_pos_y_pacman = indice_pos_y_pacman + step_y_pacman_mat
        next_indice_pos_x_pacman = indice_pos_x_pacman + step_x_pacman_mat


        if next_indice_pos_x_pacman >= largeur :
            next_indice_pos_x_pacman = 0

        if next_indice_pos_x_pacman < 0 :
            next_indice_pos_x_pacman = largeur-1

        if next_indice_pos_y_pacman >= hauteur:
            next_indice_pos_y_pacman = 0

        if next_indice_pos_y_pacman < 0:
            next_indice_pos_y_pacman = hauteur-1


        if current_mvmt_pacman != next_mvmt and mat_map[next_indice_pos_y_pacman][next_indice_pos_x_pacman] == -1 :

            next_mvmt = current_mvmt_pacman

            mvmt_charracteristics = utilities.mvmt_init(next_mvmt)
            step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
            step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
            step_x_pacman = step_x_pacman_mat * step
            step_y_pacman = step_y_pacman_mat * step
            i_pacmans = mvmt_charracteristics["i_pacmans"]

            next_indice_pos_y_pacman = indice_pos_y_pacman + step_y_pacman_mat
            next_indice_pos_x_pacman = indice_pos_x_pacman + step_x_pacman_mat


        if num_pos_fantome_0%epaisseur == 0 :

            num_pos_fantome_0=0

            indice_pos_x_fantome_0 += step_x_fantome_0_mat
            indice_pos_y_fantome_0 += step_y_fantome_0_mat

            case_haut = mat_map[indice_pos_y_fantome_0-1][indice_pos_x_fantome_0]
            case_droite = mat_map[indice_pos_y_fantome_0][indice_pos_x_fantome_0+1]
            case_gauche = mat_map[indice_pos_y_fantome_0][indice_pos_x_fantome_0-1]
            case_bas = mat_map[indice_pos_y_fantome_0+1][indice_pos_x_fantome_0]


            if case_haut<0 :
                liste_deplacements.remove("upward")

            if case_droite<0 :
                liste_deplacements.remove("rightward")

            if case_gauche<0 :
                liste_deplacements.remove("leftward")

            if case_bas<0 :
                liste_deplacements.remove("downward")

            if len(liste_deplacements)>2 :

                current_mvmt_fantome_0 = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]


            liste_deplacements = ["rightward","upward","leftward","downward"]


        mvmt_charracteristics = utilities.mvmt_init(current_mvmt_fantome_0)
        step_x_fantome_0_mat = mvmt_charracteristics["step_x_mat"]
        step_y_fantome_0_mat = mvmt_charracteristics["step_y_mat"]
        step_x_fantome_0 = step_x_fantome_0_mat * step
        step_y_fantome_0 = step_y_fantome_0_mat * step


        xpos_fantome_0 += step_x_fantome_0
        ypos_fantome_0 += step_y_fantome_0


        if mat_map[next_indice_pos_y_pacman][next_indice_pos_x_pacman] >= 0 :

            num_pos_pacman += step_x_pacman_mat + step_y_pacman_mat
            xpos_pacman += step_x_pacman
            ypos_pacman += step_y_pacman
            current_mvmt_pacman = next_mvmt


            while 0 < abs(num_pos_pacman) and abs(num_pos_pacman) < pos_per_mvmt :


                pacman = pacmans[i_pacmans][j_pacmans]
                screen.blit(pacman,[xpos_pacman,ypos_pacman])

                font=pygame.font.Font(None, 40)
                text = font.render(str(score),1,(255,255,255))
                screen.blit(text, (screen_width/2+10,16))
                screen.blit(ghost_0,[xpos_fantome_0,ypos_fantome_0])

                pygame.display.flip()

                num_pos_fantome_0 += 1
                j_pacmans += 1
                j_pacmans = j_pacmans%8


                screen.blit(map, (0,0))


                for i in range(len(mat_map)) :

                    for j in range(len(mat_map[i])) :

                        if mat_map[i][j] == 1 :

                            x_seed = tab_pos[i][j][1]
                            y_seed = tab_pos[i][j][0]

                            screen.blit(seed, (x_seed,y_seed))

                if step_x_pacman != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                                running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                current_mvmt_pacman = "leftward"

                            if event.key == pygame.K_RIGHT :
                                current_mvmt_pacman = "rightward"

                            if event.key == pygame.K_UP :
                                next_mvmt_choosed = True
                                next_mvmt = "upward"

                            if event.key == pygame.K_DOWN :
                                next_mvmt_choosed = True
                                next_mvmt = "downward"


                if step_y_pacman != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                            running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                next_mvmt_choosed = True
                                next_mvmt = "leftward"

                            if event.key == pygame.K_RIGHT :
                                next_mvmt_choosed = True
                                next_mvmt = "rightward"

                            if event.key == pygame.K_UP :
                                current_mvmt_pacman = "upward"


                            if event.key == pygame.K_DOWN :
                                current_mvmt_pacman = "downward"


                mvmt_charracteristics = utilities.mvmt_init(current_mvmt_pacman)
                step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
                step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
                step_x_pacman = step_x_pacman_mat * step
                step_y_pacman = step_y_pacman_mat * step
                i_pacmans = mvmt_charracteristics["i_pacmans"]


                xpos_pacman += step_x_pacman
                ypos_pacman += step_y_pacman
                num_pos_pacman += step_x_pacman_mat + step_y_pacman_mat


                if num_pos_fantome_0%pos_per_mvmt == 0 :

                    num_pos_fantome_0 = 0

                    indice_pos_x_fantome_0 += step_x_fantome_0_mat
                    indice_pos_y_fantome_0 += step_y_fantome_0_mat

                    case_haut = mat_map[indice_pos_y_fantome_0-1][indice_pos_x_fantome_0]
                    case_droite = mat_map[indice_pos_y_fantome_0][indice_pos_x_fantome_0+1]
                    case_gauche = mat_map[indice_pos_y_fantome_0][indice_pos_x_fantome_0-1]
                    case_bas = mat_map[indice_pos_y_fantome_0+1][indice_pos_x_fantome_0]

                    if case_haut<0 :
                        liste_deplacements.remove("upward")

                    if case_droite<0 :
                        liste_deplacements.remove("rightward")

                    if case_gauche<0 :
                        liste_deplacements.remove("leftward")

                    if case_bas<0 :
                        liste_deplacements.remove("downward")

                    if len(liste_deplacements)>2 :

                        current_mvmt_fantome_0 = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]

                    liste_deplacements = ["rightward","upward","leftward","downward"]

                mvmt_charracteristics = utilities.mvmt_init(current_mvmt_fantome_0)
                step_x_fantome_0_mat = mvmt_charracteristics["step_x_mat"]
                step_y_fantome_0_mat = mvmt_charracteristics["step_y_mat"]
                step_x_fantome_0 = step_x_fantome_0_mat * step
                step_y_fantome_0 = step_y_fantome_0_mat * step


                xpos_fantome_0 += step_x_fantome_0
                ypos_fantome_0 += step_y_fantome_0



            if next_indice_pos_x_pacman >= largeur :
                xpos_pacman = 0 #-pacman_size

            if next_indice_pos_x_pacman < 0 :
                xpos_pacman = screen_widths-1

            if next_indice_pos_y_pacman >= hauteur:
                ypos_pacman = -pacman_sizes

            if next_indice_pos_y_pacman < 0:
                ypos_pacman = screen_heights



            if num_pos_pacman != 0 :

                indice_pos_x_pacman = next_indice_pos_x_pacman
                indice_pos_y_pacman = next_indice_pos_y_pacman

                if mat_map[next_indice_pos_y_pacman][next_indice_pos_x_pacman] != 0 :

                    mat_map[next_indice_pos_y_pacman][next_indice_pos_x_pacman] = mat_map[next_indice_pos_y_pacman][next_indice_pos_x_pacman]*0
                    score += 1

                num_pos_pacman = 0

        pacman = pacmans[i_pacmans][j_pacmans]
        screen.blit(pacman,[xpos_pacman,ypos_pacman])
        screen.blit(ghost_0,[xpos_fantome_0,ypos_fantome_0])

        font=pygame.font.Font(None, 40)
        text = font.render(str(score),1,(255,255,255))
        screen.blit(text, (screen_width/2+10,16))


        pygame.display.flip()

        screen.blit(map, (0,0))


        for i in range(len(mat_map)) :

            for j in range(len(mat_map[i])) :

                if mat_map[i][j] == 1 :

                    x_seed = tab_pos[i][j][1]
                    y_seed = tab_pos[i][j][0]

                screen.blit(seed, (x_seed,y_seed))



if __name__=="__main__":
    main()
