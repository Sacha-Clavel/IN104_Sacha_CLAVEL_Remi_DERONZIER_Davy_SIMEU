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


    # Largeur et hauteur de la fenêtre

    screen_width = 606
    screen_height = 775

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((screen_width,screen_height))
    map_org = pygame.image.load("images/map.png")
    map = pygame.transform.scale(map_org,[screen_width,screen_height])
    screen.blit(map, [0,0])

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice images_pacman contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

    pacman_size = 32

    images_pacman = []

    for i in range(0,360,90):
        line_images_pacman = []

        for j in range(8):
            pacman_org = pygame.image.load("images/pacman"+str(j)+".png")
            pacman_rotated = pygame.transform.rotate(pacman_org,i)

            pacman = pygame.transform.scale(pacman_rotated,[pacman_size,pacman_size])

            line_images_pacman.append(pacman)

        images_pacman.append(line_images_pacman)


    # Creation des images des fantomes

        ghosts_size = 30

        image_shadow_px = pygame.image.load("images/shadow.png")
        image_shadow = pygame.transform.scale(image_shadow_px,[ghosts_size,ghosts_size])


    # Création des images des graines

    seed_size = 10

    seed_px = pygame.image.load("Images/seed.png")
    seed = pygame.transform.scale(seed_px,[seed_size,seed_size])


    # Creation de la matrice représentant la carte et de la matrice regroupant les positions sur l'écran correspondant à chaque case de matrice

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




    pos_per_mvmt = 9
    STEP = 3
    epaisseur = STEP*pos_per_mvmt


    largeur = 23
    hauteur = 27

    offset_x = 1
    offset_y = 61

    tab_pos = [[[offset_x + i*epaisseur,offset_y + j*epaisseur] for i in range(largeur)] for j in range(hauteur)]

    # Methode affichant les graines présentes sur la carte

    def draw_seed():

        for i in range(len(mat_map)) :

            for j in range(len(mat_map[i])) :

                if mat_map[i][j] == 1 :

                    x_seed = tab_pos[i][j][0]
                    y_seed = tab_pos[i][j][1]

                    screen.blit(seed, (x_seed,y_seed))


    # Initialisations des personnages



    i_pacmans = 0

    liste_deplacements = ["rightward","upward","leftward","downward"]

    index_i_pacman = 20
    index_j_pacman = 11

    offset_pacman_x = 11
    offset_pacman_y = 11

    pos_x = tab_pos[index_i_pacman][index_j_pacman][0] - offset_pacman_x
    pos_y = tab_pos[index_i_pacman][index_j_pacman][1] - offset_pacman_y

    player = utilities.pacman(pos_x,pos_y,index_i_pacman,index_j_pacman,"leftward",0,images_pacman,0)

    index_j_shadow = 1
    index_i_shadow = 1

    offset_fantome_0_x = 10
    offset_fantome_0_y = 10

    pos_x_shadow = tab_pos[index_i_shadow][index_j_shadow][0] - offset_fantome_0_x
    pos_y_shadow = tab_pos[index_i_shadow][index_j_shadow][1] - offset_fantome_0_y

    shadow = utilities.ghost(pos_x_shadow,pos_y_shadow,index_i_shadow,index_j_shadow,"rightward",0,"shadow",image_shadow)
    #speedy =
    #bashful =
    #pokey =



    player.direction = "leftward"
    next_direction_choosed = True
    next_direction = "leftward"

    step_x_pacman = -STEP
    step_y_pacman = 0
    step_x_pacman_mat = -1
    step_y_pacman_mat = 0


    current_mvmt_shadow = liste_deplacements[0] # "rightward"

    step_x_fantome_0 = STEP
    step_y_fantome_0 = 0
    step_x_fantome_0_mat = 1
    step_y_fantome_0_mat = 0


    score = 0



    # Initialisation de l'affichage

    image_pacman = images_pacman[i_pacmans][player.n_mouth]

    screen.blit(map, [0,0])

    player.draw(screen)
    shadow.draw(screen)


    draw_seed()

    pygame.display.flip()

    while running:

        # 1st Management of ghost movements

        shadow.n_pos += 1

        if shadow.n_pos%pos_per_mvmt == 0 :

            shadow.n_pos=0

            shadow.update_indexes()

            case_haut = mat_map[shadow.index_i-1][shadow.index_j]
            case_droite = mat_map[shadow.index_i][shadow.index_j+1]
            case_gauche = mat_map[shadow.index_i][shadow.index_j-1]
            case_bas = mat_map[shadow.index_i+1][shadow.index_j]


            if case_haut<0 :
                liste_deplacements.remove("upward")

            if case_droite<0 :
                liste_deplacements.remove("rightward")

            if case_gauche<0 :
                liste_deplacements.remove("leftward")

            if case_bas<0 :
                liste_deplacements.remove("downward")

            if len(liste_deplacements)>2 :

                current_mvmt_shadow = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]

            liste_deplacements = ["rightward","upward","leftward","downward"]

        shadow.config_mvmt(current_mvmt_shadow)
        shadow.move()

        # 1st Management of player movements

        player.n_pos = 0
        player.n_mouth += 1
        player.n_mouth = player.n_mouth%8


        if next_direction_choosed :
            next_direction_choosed = False

        else :

            next_direction = player.direction

            for event in pygame.event.get():

                # Condition de sortie

                if event.type == pygame.QUIT:
                    running = False

                    # Déplacements du pacman en fonction des entrées claviers

                if event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_LEFT:
                        next_direction = "leftward"

                    if event.key == pygame.K_RIGHT :
                        next_direction = "rightward"

                    if event.key == pygame.K_UP :
                        next_direction = "upward"

                    if event.key == pygame.K_DOWN :
                        next_direction = "downward"


        precedent_player_direction = player.direction
        player.config_mvmt(next_direction)

        potential_next_index_i_player, potential_next_index_j_player = player.potential_update_of_indexes()


        if potential_next_index_j_player >= largeur :
            potential_next_index_j_player = 0

        if potential_next_index_j_player < 0 :
            potential_next_index_j_player = largeur-1

        if potential_next_index_i_player >= hauteur:
            potential_next_index_i_player = 0

        if potential_next_index_i_player < 0:
            potential_next_index_i_player = hauteur-1


        if player.direction != precedent_player_direction and mat_map[potential_next_index_i_player][potential_next_index_j_player] == -1 :

            next_direction = precedent_player_direction
            player.config_mvmt(next_direction)

            potential_next_index_i_player, potential_next_index_j_player = player.potential_update_of_indexes()


        if mat_map[potential_next_index_i_player][potential_next_index_j_player] >= 0 :

            player.n_pos += player.step_i + player.step_j
            player.move()


            while 0 < abs(player.n_pos) and abs(player.n_pos) < pos_per_mvmt :


                player.draw(screen)
                shadow.draw(screen)

                font=pygame.font.Font(None, 40)
                text = font.render(str(score),1,(255,255,255))
                screen.blit(text, (screen_width/2+10,16))

                pygame.display.flip()

                screen.blit(map, (0,0))
                draw_seed()

                shadow.n_pos += 1
                player.n_mouth += 1
                player.n_mouth = player.n_mouth%8

                if player.index_j != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                                running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                player.direction = "leftward"

                            if event.key == pygame.K_RIGHT :
                                player.direction = "rightward"

                            if event.key == pygame.K_UP :
                                next_direction_choosed = True
                                next_direction = "upward"

                            if event.key == pygame.K_DOWN :
                                next_direction_choosed = True
                                next_direction = "downward"


                if player.step_i != 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                            running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                next_direction_choosed = True
                                next_direction = "leftward"

                            if event.key == pygame.K_RIGHT :
                                next_direction_choosed = True
                                next_direction = "rightward"

                            if event.key == pygame.K_UP :
                                player.direction = "upward"

                            if event.key == pygame.K_DOWN :
                                player.direction = "downward"


                player.config_mvmt(player.direction)
                player.move()

                player.n_pos += player.step_i + player.step_j


                if shadow.n_pos%pos_per_mvmt == 0 :

                    shadow.n_pos = 0

                    shadow.update_indexes()

                    case_haut = mat_map[shadow.index_i-1][shadow.index_j]
                    case_droite = mat_map[shadow.index_i][shadow.index_j+1]
                    case_gauche = mat_map[shadow.index_i][shadow.index_j-1]
                    case_bas = mat_map[shadow.index_i+1][shadow.index_j]


                    if case_haut<0 :
                        liste_deplacements.remove("upward")

                    if case_droite<0 :
                        liste_deplacements.remove("rightward")

                    if case_gauche<0 :
                        liste_deplacements.remove("leftward")

                    if case_bas<0 :
                        liste_deplacements.remove("downward")

                    if len(liste_deplacements)>2 :

                        current_mvmt_shadow = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]

                    liste_deplacements = ["rightward","upward","leftward","downward"]

                    shadow.config_mvmt(current_mvmt_shadow)
                    shadow.move()


            if potential_next_index_j_player >= largeur :
                player.pos_x = 0 #-pacman_size

            if potential_next_index_j_player < 0 :
                player.pos_x = screen_widths-1

            if potential_next_index_i_player >= hauteur:
                player.pos_y = -pacman_sizes

            if potential_next_index_i_player < 0:
                player.pos_y = screen_heights



            player.potential_update_of_indexes()

            if mat_map[player.index_i][player.index_j] != 0 :

                mat_map[player.index_i][player.index_j] *= 0
                score += 1


        player.draw(screen)
        shadow.draw(screen)

        font=pygame.font.Font(None, 40)
        text = font.render(str(score),1,(255,255,255))
        screen.blit(text, (screen_width/2+10,16))

        pygame.display.flip()

        screen.blit(map, (0,0))
        draw_seed()


if __name__=="__main__":
    main()








########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################












# import pygame
# import random as rd
# import utilities
#
# # Taille matrice carte : 27x23
#
#
# def main() :
#
#     pygame.init()
#     running = True
#
#     # Affichages divers (logo, titre de la fenêtre ...)
#
#     logo = pygame.image.load("images/pacman10.png")
#     pygame.display.set_icon(logo)
#     pygame.display.set_caption("Pacman")
#
#     # Creation de l'image Dot (Point pour mesurer la largeur des murs)
#
#         #Dot = pygame.image.load("Images/Dot.png")
#
#     # Largeur et hauteur de la fenêtre
#
#     screen_width = 606
#     screen_height = 775
#
#     # Création de la fenêtre et initialisation du fond (La carte de pacman)
#
#     screen = pygame.display.set_mode((screen_width,screen_height))
#     map_org = pygame.image.load("images/map.png")
#     map = pygame.transform.scale(map_org,[screen_width,screen_height]) #Ajustement de l'image de fond
#     screen.blit(map, [0,0])
#
#     # Initialisation du pacman et création des diverses formes de bouche du pacman
#     # La matrice Pacmans contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés
#
#     pacman_size = 32
#
#
#
#     pacmans = []
#
#     for i in range(0,360,90):
#         pacman_ligne = []
#
#         for j in range(8):
#             pacman_org = pygame.image.load("images/pacman"+str(j)+".png")
#             pacman_rotated = pygame.transform.rotate(pacman_org,i)
#             pacman = pygame.transform.scale(pacman_rotated,[pacman_size,pacman_size])
#             pacman_ligne.append(pacman)
#         pacmans.append(pacman_ligne)
#
#     i_pacmans = 0
#     player.n_mouth = 0
#
#     # Création des images graines
#
#     seed_size = 10
#
#     seed_px = pygame.image.load("Images/seed.png")
#     seed = pygame.transform.scale(seed_px,[seed_size,seed_size])
#
# # Creation des images des fantomes
#
#     ghosts_size = 30
#
#     image_shadow_px = pygame.image.load("images/ghost0.png")
#     image_shadow = pygame.transform.scale(image_shadow_px,[ghosts_size,ghosts_size])
#
#
#     # Creation de la matrice représentant la carte et de la matrice des positions de chaque case matrice
#
#     mat_map = [     [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                     [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
#                     [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
#                     [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
#                     [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
#                     [-1,  1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1,  1, -1],
#                     [-1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [ 1,  1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1,  1,  1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1],
#                     [-1,  1,  1,  1,  1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1,  1,  1,  1, -1],
#                     [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1,  1, -1],
#                     [-1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1,  0,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1, -1],
#                     [-1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1],
#                     [-1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1,  1, -1, -1, -1],
#                     [-1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1, -1],
#                     [-1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1],
#                     [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
#                     [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  ]
#
#
#     offset_x = 1
#     offset_y = 61
#
#     pos_per_mvmt = 9
#     STEP = 3
#     epaisseur = STEP*pos_per_mvmt
#     player.n_pos = 0
#     shadow.n_pos = 0
#
#     largeur = 23
#     hauteur = 27
#
#     tab_pos = [[[offset_y + j*epaisseur,offset_x + i*epaisseur] for i in range(largeur)] for j in range(hauteur)]
#
#
#     # Paramètre de positons et de vitesse
#
#     liste_deplacements = ["rightward","upward","leftward","downward"]
#
#     index_i_pacman = 20
#     index_j_pacman = 11
#
#     index_j_shadow = 1
#     index_i_shadow = 1
#
#
#     offset_pacman_x = 11
#     offset_pacman_y = 11
#
#     offset_fantome_0_x = 10
#     offset_fantome_0_y = 10
#
#     player.pos_x = tab_pos[index_i_pacman][index_j_pacman][1] - offset_pacman_x
#     player.pos_y = tab_pos[index_i_pacman][index_j_pacman][0] - offset_pacman_y
#
#     pos_x_shadow = tab_pos[index_i_shadow][index_j_shadow][1] - offset_fantome_0_x
#     pos_y_shadow = tab_pos[index_i_shadow][index_j_shadow][0] - offset_fantome_0_y
#
#
#
#     player.direction = "leftward"
#     next_direction_choosed = True
#     next_direction = "leftward"
#
#     step_x_pacman = STEP
#     step_y_pacman = 0
#     step_x_pacman_mat = 1
#     step_y_pacman_mat = 0
#
#
#     current_mvmt_shadow = liste_deplacements[0] # "rightward"
#
#     step_x_fantome_0 = STEP
#     step_y_fantome_0 = 0
#     step_x_fantome_0_mat = 1
#     step_y_fantome_0_mat = 0
#
#
#     score = 0
#
#
#     # Initialisation de l'affichage
#
#     pacman = pacmans[i_pacmans][player.n_mouth]
#
#     screen.blit(map, [0,0])
#
#     screen.blit(pacman,[player.pos_x,player.pos_y])
#
#
#     for i in range(len(mat_map)) :
#
#         for j in range(len(mat_map[i])) :
#
#             if mat_map[i][j] == 1 :
#
#                 x_seed = tab_pos[i][j][1]
#                 y_seed = tab_pos[i][j][0]
#
#                 screen.blit(seed, (x_seed,y_seed))
#
#
#
#     pygame.display.flip()
#
#     while running:
#
#         shadow.n_pos += 1
#         player.n_mouth += 1
#         player.n_mouth = player.n_mouth%8
#
#         if next_direction_choosed :
#             next_direction_choosed = False
#             #next_direction = None
#
#         else :
#
#             next_direction = player.direction
#
#             for event in pygame.event.get():
#
#                 # Condition de sortie
#
#                 if event.type == pygame.QUIT:
#                     running = False
#
#                     # Déplacements du pacman en fonction des entrées claviers
#
#                 if event.type == pygame.KEYDOWN :
#
#                     if event.key == pygame.K_LEFT:
#                         next_direction = "leftward"
#
#                     if event.key == pygame.K_RIGHT :
#                         next_direction = "rightward"
#
#                     if event.key == pygame.K_UP :
#                         next_direction = "upward"
#
#                     if event.key == pygame.K_DOWN :
#                         next_direction = "downward"
#
#
#         mvmt_charracteristics = utilities.mvmt_init(next_direction)
#         step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
#         step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
#         step_x_pacman = step_x_pacman_mat * STEP
#         step_y_pacman = step_y_pacman_mat * STEP
#         i_pacmans = mvmt_charracteristics["i_pacmans"]
#
#
#         potential_next_index_i_player = index_i_pacman + step_y_pacman_mat
#         potential_next_index_j_player = index_j_pacman + step_x_pacman_mat
#
#
#         if potential_next_index_j_player >= largeur :
#             potential_next_index_j_player = 0
#
#         if potential_next_index_j_player < 0 :
#             potential_next_index_j_player = largeur-1
#
#         if potential_next_index_i_player >= hauteur:
#             potential_next_index_i_player = 0
#
#         if potential_next_index_i_player < 0:
#             potential_next_index_i_player = hauteur-1
#
#
#         if player.direction != next_direction and mat_map[potential_next_index_i_player][potential_next_index_j_player] == -1 :
#
#             next_direction = player.direction
#
#             mvmt_charracteristics = utilities.mvmt_init(next_direction)
#             step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
#             step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
#             step_x_pacman = step_x_pacman_mat * STEP
#             step_y_pacman = step_y_pacman_mat * STEP
#             i_pacmans = mvmt_charracteristics["i_pacmans"]
#
#             potential_next_index_i_player = index_i_pacman + step_y_pacman_mat
#             potential_next_index_j_player = index_j_pacman + step_x_pacman_mat
#
#
#         if shadow.n_pos%pos_per_mvmt == 0 :
#
#             shadow.n_pos=0
#
#             index_j_shadow += step_x_fantome_0_mat
#             index_i_shadow += step_y_fantome_0_mat
#
#             case_haut = mat_map[index_i_shadow-1][index_j_shadow]
#             case_droite = mat_map[index_i_shadow][index_j_shadow+1]
#             case_gauche = mat_map[index_i_shadow][index_j_shadow-1]
#             case_bas = mat_map[index_i_shadow+1][index_j_shadow]
#
#
#             if case_haut<0 :
#                 liste_deplacements.remove("upward")
#
#             if case_droite<0 :
#                 liste_deplacements.remove("rightward")
#
#             if case_gauche<0 :
#                 liste_deplacements.remove("leftward")
#
#             if case_bas<0 :
#                 liste_deplacements.remove("downward")
#
#             if len(liste_deplacements)>2 :
#
#                 current_mvmt_shadow = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]
#
#
#             liste_deplacements = ["rightward","upward","leftward","downward"]
#
#
#         mvmt_charracteristics = utilities.mvmt_init(current_mvmt_shadow)
#         step_x_fantome_0_mat = mvmt_charracteristics["step_x_mat"]
#         step_y_fantome_0_mat = mvmt_charracteristics["step_y_mat"]
#         step_x_fantome_0 = step_x_fantome_0_mat * STEP
#         step_y_fantome_0 = step_y_fantome_0_mat * STEP
#
#
#         pos_x_shadow += step_x_fantome_0
#         pos_y_shadow += step_y_fantome_0
#
#
#         if mat_map[potential_next_index_i_player][potential_next_index_j_player] >= 0 :
#
#             player.n_pos += step_x_pacman_mat + step_y_pacman_mat
#             player.pos_x += step_x_pacman
#             player.pos_y += step_y_pacman
#             player.direction = next_direction
#
#
#             while 0 < abs(player.n_pos) and abs(player.n_pos) < pos_per_mvmt :
#
#
#                 pacman = pacmans[i_pacmans][player.n_mouth]
#                 screen.blit(pacman,[player.pos_x,player.pos_y])
#
#                 font=pygame.font.Font(None, 40)
#                 text = font.render(str(score),1,(255,255,255))
#                 screen.blit(text, (screen_width/2+10,16))
#                 screen.blit(image_shadow,[pos_x_shadow,pos_y_shadow])
#
#                 pygame.display.flip()
#
#                 shadow.n_pos += 1
#                 player.n_mouth += 1
#                 player.n_mouth = player.n_mouth%8
#
#
#                 screen.blit(map, (0,0))
#
#
#                 for i in range(len(mat_map)) :
#
#                     for j in range(len(mat_map[i])) :
#
#                         if mat_map[i][j] == 1 :
#
#                             x_seed = tab_pos[i][j][1]
#                             y_seed = tab_pos[i][j][0]
#
#                             screen.blit(seed, (x_seed,y_seed))
#
#                 if step_x_pacman != 0 :
#
#                     for event in pygame.event.get():
#
#                         # Condition de sortie
#
#                         if event.type == pygame.QUIT:
#                                 running = False
#
#                         # Déplacements du pacman en fonction des entrées claviers
#
#                         if event.type == pygame.KEYDOWN :
#
#                             if event.key == pygame.K_LEFT:
#                                 player.direction = "leftward"
#
#                             if event.key == pygame.K_RIGHT :
#                                 player.direction = "rightward"
#
#                             if event.key == pygame.K_UP :
#                                 next_direction_choosed = True
#                                 next_direction = "upward"
#
#                             if event.key == pygame.K_DOWN :
#                                 next_direction_choosed = True
#                                 next_direction = "downward"
#
#
#                 if step_y_pacman != 0 :
#
#                     for event in pygame.event.get():
#
#                         # Condition de sortie
#
#                         if event.type == pygame.QUIT:
#                             running = False
#
#                         # Déplacements du pacman en fonction des entrées claviers
#
#                         if event.type == pygame.KEYDOWN :
#
#                             if event.key == pygame.K_LEFT:
#                                 next_direction_choosed = True
#                                 next_direction = "leftward"
#
#                             if event.key == pygame.K_RIGHT :
#                                 next_direction_choosed = True
#                                 next_direction = "rightward"
#
#                             if event.key == pygame.K_UP :
#                                 player.direction = "upward"
#
#
#                             if event.key == pygame.K_DOWN :
#                                 player.direction = "downward"
#
#
#                 mvmt_charracteristics = utilities.mvmt_init(player.direction)
#                 step_x_pacman_mat = mvmt_charracteristics["step_x_mat"]
#                 step_y_pacman_mat = mvmt_charracteristics["step_y_mat"]
#                 step_x_pacman = step_x_pacman_mat * STEP
#                 step_y_pacman = step_y_pacman_mat * STEP
#                 i_pacmans = mvmt_charracteristics["i_pacmans"]
#
#
#                 player.pos_x += step_x_pacman
#                 player.pos_y += step_y_pacman
#                 player.n_pos += step_x_pacman_mat + step_y_pacman_mat
#
#
#                 if shadow.n_pos%pos_per_mvmt == 0 :
#
#                     shadow.n_pos = 0
#
#                     index_j_shadow += step_x_fantome_0_mat
#                     index_i_shadow += step_y_fantome_0_mat
#
#                     case_haut = mat_map[index_i_shadow-1][index_j_shadow]
#                     case_droite = mat_map[index_i_shadow][index_j_shadow+1]
#                     case_gauche = mat_map[index_i_shadow][index_j_shadow-1]
#                     case_bas = mat_map[index_i_shadow+1][index_j_shadow]
#
#                     if case_haut<0 :
#                         liste_deplacements.remove("upward")
#
#                     if case_droite<0 :
#                         liste_deplacements.remove("rightward")
#
#                     if case_gauche<0 :
#                         liste_deplacements.remove("leftward")
#
#                     if case_bas<0 :
#                         liste_deplacements.remove("downward")
#
#                     if len(liste_deplacements)>2 :
#
#                         current_mvmt_shadow = liste_deplacements[rd.randint(0,len(liste_deplacements)-1)]
#
#                     liste_deplacements = ["rightward","upward","leftward","downward"]
#
#                 mvmt_charracteristics = utilities.mvmt_init(current_mvmt_shadow)
#                 step_x_fantome_0_mat = mvmt_charracteristics["step_x_mat"]
#                 step_y_fantome_0_mat = mvmt_charracteristics["step_y_mat"]
#                 step_x_fantome_0 = step_x_fantome_0_mat * STEP
#                 step_y_fantome_0 = step_y_fantome_0_mat * STEP
#
#
#                 pos_x_shadow += step_x_fantome_0
#                 pos_y_shadow += step_y_fantome_0
#
#             if potential_next_index_j_player >= largeur :
#                 player.pos_x = 0 #-pacman_size
#
#             if potential_next_index_j_player < 0 :
#                 player.pos_x = screen_widths-1
#
#             if potential_next_index_i_player >= hauteur:
#                 player.pos_y = -pacman_sizes
#
#             if potential_next_index_i_player < 0:
#                 player.pos_y = screen_heights
#
#
#
#             if player.n_pos != 0 :
#
#                 index_j_pacman = potential_next_index_j_player
#                 index_i_pacman = potential_next_index_i_player
#
#                 if mat_map[potential_next_index_i_player][potential_next_index_j_player] != 0 :
#
#                     mat_map[potential_next_index_i_player][potential_next_index_j_player] = mat_map[potential_next_index_i_player][potential_next_index_j_player]*0
#                     score += 1
#
#                 player.n_pos = 0
#
#         pacman = pacmans[i_pacmans][player.n_mouth]
#         screen.blit(pacman,[player.pos_x,player.pos_y])
#         screen.blit(image_shadow,[pos_x_shadow,pos_y_shadow])
#
#         font=pygame.font.Font(None, 40)
#         text = font.render(str(score),1,(255,255,255))
#         screen.blit(text, (screen_width/2+10,16))
#
#
#         pygame.display.flip()
#
#         screen.blit(map, (0,0))
#
#
#         for i in range(len(mat_map)) :
#
#             for j in range(len(mat_map[i])) :
#
#                 if mat_map[i][j] == 1 :
#
#                     x_seed = tab_pos[i][j][1]
#                     y_seed = tab_pos[i][j][0]
#
#                 screen.blit(seed, (x_seed,y_seed))
#
#
#
# if __name__=="__main__":
#     main()
