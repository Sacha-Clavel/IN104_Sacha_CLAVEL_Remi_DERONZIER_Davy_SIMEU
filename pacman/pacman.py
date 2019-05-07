import pygame
import random as rd
import utilities

# Taille matrice carte : 27x23


def main() :

    pygame.init()
    running = True

    # Affichages divers (logo, titre de la fenêtre ...)

    logo = pygame.image.load("images/pacman.png")
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

    # Initialisation des graines

    seed_size = 10

    seed_px = pygame.image.load("Images/seed.png")
    seed = pygame.transform.scale(seed_px,[seed_size,seed_size])


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

    epaisseur = 27

    largeur = 23
    hauteur = 27

    tab_pos = [[[offset_y + j*epaisseur,offset_x + i*epaisseur] for i in range(largeur)] for j in range(hauteur)]


    # Paramètre de positons et de vitesse

    indice_pos_y = 20
    indice_pos_x = 11

    offset_pacman_x = 11
    offset_pacman_y = 11

    xpos = tab_pos[indice_pos_y][indice_pos_x][1] - offset_pacman_x
    ypos = tab_pos[indice_pos_y][indice_pos_x][0] - offset_pacman_y

    step = 3
    pos_per_mvmt = epaisseur/step
    num_pos = 0

    current_mvmt = "left"
    next_mvmt_choosed = True
    next_mvmt = "left"

    step_x = step
    step_y = 0
    step_x_mat = 1
    step_y_mat = 0




    score = 0


    # Initialisation de l'affichage

    pacman = pacmans[i_pacmans][j_pacmans]

    screen.blit(map, [0,0])

    screen.blit(pacman,[xpos,ypos])


    for i in range(len(mat_map)) :

        for j in range(len(mat_map[i])) :

            if mat_map[i][j] == 1 :

                x_seed = tab_pos[i][j][1]
                y_seed = tab_pos[i][j][0]

                screen.blit(seed, (x_seed,y_seed))



    pygame.display.flip()

    while running:

        j_pacmans += 1
        j_pacmans = j_pacmans%8

        if next_mvmt_choosed :
            next_mvmt_choosed = False
            #next_mvmt = None

        else :

            next_mvmt = current_mvmt

            for event in pygame.event.get():

                # Condition de sortie

                if event.type == pygame.QUIT:
                    running = False

                    # Déplacements du pacman en fonction des entrées claviers

                if event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_LEFT:
                        next_mvmt = "left"

                    if event.key == pygame.K_RIGHT :
                        next_mvmt = "right"

                    if event.key == pygame.K_UP :
                        next_mvmt = "up"

                    if event.key == pygame.K_DOWN :
                        next_mvmt = "down"

        mvmt_charracteristics = utilities.mvmt_init(next_mvmt)
        step_x_mat = mvmt_charracteristics["step_x_mat"]
        step_y_mat = mvmt_charracteristics["step_y_mat"]
        step_x = step_x_mat * step
        step_y = step_y_mat * step
        i_pacmans = mvmt_charracteristics["i_pacmans"]

        next_indice_pos_y = indice_pos_y + step_y_mat
        next_indice_pos_x = indice_pos_x + step_x_mat


        if xpos > screen_width or next_indice_pos_x >= largeur :
            xpos = -pacman_size
            next_indice_pos_x = 0

        if xpos < -pacman_size or next_indice_pos_x < 0 :
            xpos = screen_width
            next_indice_pos_x = largeur-1

        if ypos > screen_height or next_indice_pos_y >= hauteur:
            ypos = -pacman_size
            next_indice_pos_y = 0

        if ypos < -pacman_size or next_indice_pos_y < 0:
            ypos = screen_height
            next_indice_pos_y = hauteur-1


        if current_mvmt != next_mvmt and mat_map[next_indice_pos_y][next_indice_pos_x] == -1 :

            next_mvmt = current_mvmt

            mvmt_charracteristics = utilities.mvmt_init(next_mvmt)
            step_x_mat = mvmt_charracteristics["step_x_mat"]
            step_y_mat = mvmt_charracteristics["step_y_mat"]
            step_x = step_x_mat * step
            step_y = step_y_mat * step
            i_pacmans = mvmt_charracteristics["i_pacmans"]

            next_indice_pos_y = indice_pos_y + step_y_mat
            next_indice_pos_x = indice_pos_x + step_x_mat


        if mat_map[next_indice_pos_y][next_indice_pos_x] >= 0 :

            num_pos += step_x_mat + step_y_mat
            xpos += step_x
            ypos += step_y
            current_mvmt = next_mvmt


            while 0 < abs(num_pos) and abs(num_pos) < pos_per_mvmt :

                j_pacmans += 1
                j_pacmans = j_pacmans%8

                pacman = pacmans[i_pacmans][j_pacmans]
                screen.blit(pacman,[xpos,ypos])

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

                if step_x != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                                running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                current_mvmt = "left"

                            if event.key == pygame.K_RIGHT :
                                current_mvmt = "right"

                            if event.key == pygame.K_UP :
                                next_mvmt_choosed = True
                                next_mvmt = "up"

                            if event.key == pygame.K_DOWN :
                                next_mvmt_choosed = True
                                next_mvmt = "down"


                if step_y != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                            running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                next_mvmt_choosed = True
                                next_mvmt = "left"

                            if event.key == pygame.K_RIGHT :
                                next_mvmt_choosed = True
                                next_mvmt = "right"

                            if event.key == pygame.K_UP :
                                current_mvmt = "up"


                            if event.key == pygame.K_DOWN :
                                current_mvmt = "down"


                mvmt_charracteristics = utilities.mvmt_init(current_mvmt)
                step_x_mat = mvmt_charracteristics["step_x_mat"]
                step_y_mat = mvmt_charracteristics["step_y_mat"]
                step_x = step_x_mat * step
                step_y = step_y_mat * step
                i_pacmans = mvmt_charracteristics["i_pacmans"]

                xpos += step_x
                ypos += step_y
                num_pos += step_x_mat + step_y_mat


            if num_pos != 0 :

                indice_pos_x = next_indice_pos_x
                indice_pos_y = next_indice_pos_y

                if mat_map[next_indice_pos_y][next_indice_pos_x] != 0 :

                    mat_map[next_indice_pos_y][next_indice_pos_x] = mat_map[next_indice_pos_y][next_indice_pos_x]*0
                    score += 1

                num_pos = 0

        pacman = pacmans[i_pacmans][j_pacmans]
        screen.blit(pacman,[xpos,ypos])

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
