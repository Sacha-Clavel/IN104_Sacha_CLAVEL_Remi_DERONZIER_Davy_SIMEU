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


    # Larger et hauter de la fenêtre

    SCREEN_WIDTH = 606
    SCREEN_HEIGHT = 775

    # Création de la fenêtre et initialisation du fond (La carte de pacman)

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    map_org = pygame.image.load("images/map.png")
    map = pygame.transform.scale(map_org,[SCREEN_WIDTH,SCREEN_HEIGHT])
    screen.blit(map, [0,0])

    # Initialisation du pacman et création des diverses formes de bouche du pacman
    # La matrice images_pacman contient toutes les formes du bouches du pacman toutes tournées à 0,90,180,270 degrés

    PACMAN_SIZE = 32

    images_pacman = []

    for i in range(0,360,90):
        line_images_pacman = []

        for j in range(8):
            pacman_org = pygame.image.load("images/pacman"+str(j)+".png")
            pacman_rotated = pygame.transform.rotate(pacman_org,i)

            pacman = pygame.transform.scale(pacman_rotated,[PACMAN_SIZE,PACMAN_SIZE])

            line_images_pacman.append(pacman)

        images_pacman.append(line_images_pacman)


    # Creation des images des fantomes

    GHOSTS_SIZE = 31

    image_shadow_px = pygame.image.load("images/shadow.png")
    image_shadow = pygame.transform.scale(image_shadow_px,[GHOSTS_SIZE,GHOSTS_SIZE])


    # Création des images des graines

    SEED_SIZE = 10

    seed_px = pygame.image.load("Images/seed.png")
    seed = pygame.transform.scale(seed_px,[SEED_SIZE,SEED_SIZE])


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




    POS_PER_MVMT = 9
    STEP = 3
    THICK = STEP*POS_PER_MVMT


    WIDTH = 23
    HEIGHT = 27

    OFFSET_X = 1
    OFFSET_Y = 61

    mat_pos = [[[OFFSET_X + j*THICK, OFFSET_Y + i*THICK] for j in range(WIDTH)] for i in range(HEIGHT)]

    # Methode affichant les graines présentes sur la carte

    def draw_seed():

        for i in range(len(mat_map)) :

            for j in range(len(mat_map[i])) :

                if mat_map[i][j] == 1 :

                    x_seed = mat_pos[i][j][0]
                    y_seed = mat_pos[i][j][1]

                    screen.blit(seed, (x_seed,y_seed))


    # Initialisations des personnages



    i_pacmans = 0

    direction_list = ["rightward","upward","leftward","downward"]

    index_i_pacman = 20
    index_j_pacman = 11

    OFFSET_PACMAN_X = 11
    OFFSET_PACMAN_Y = 11

    pos_x = mat_pos[index_i_pacman][index_j_pacman][0] - OFFSET_PACMAN_X
    pos_y = mat_pos[index_i_pacman][index_j_pacman][1] - OFFSET_PACMAN_Y

    player = utilities.pacman(pos_x,pos_y,index_i_pacman,index_j_pacman,"leftward",0,OFFSET_PACMAN_X,OFFSET_PACMAN_Y,images_pacman,0,None,False)

    index_j_shadow = 3
    index_i_shadow = 12

    OFFSET_GHOSTS_X = 7
    OFFSET_GHOSTS_Y = 11

    pos_x_shadow = mat_pos[index_i_shadow][index_j_shadow][0] - OFFSET_GHOSTS_X
    pos_y_shadow = mat_pos[index_i_shadow][index_j_shadow][1] - OFFSET_GHOSTS_Y

    shadow = utilities.ghost(pos_x_shadow,pos_y_shadow,index_i_shadow,index_j_shadow,"leftward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"shadow",image_shadow)
    #speedy =
    #bashful =
    #pokey =


    score = 0


    # Initialisation de l'affichage


    screen.blit(map, [0,0])

    player.draw(screen)
    shadow.draw(screen)


    draw_seed()

    pygame.display.flip()

    while running:

        # 1st Management of ghost movements

        shadow.n_pos += 1

        if shadow.n_pos == POS_PER_MVMT :

            shadow.potential_update_of_indexes_and_positions()

            pos_up = mat_map[(shadow.index_i-1)%HEIGHT][(shadow.index_j)%WIDTH]
            pos_right = mat_map[(shadow.index_i)%HEIGHT][(shadow.index_j+1)%WIDTH]
            pos_left = mat_map[(shadow.index_i)%HEIGHT][(shadow.index_j-1)%WIDTH]
            pos_down = mat_map[(shadow.index_i+1)%HEIGHT][(shadow.index_j)%WIDTH]


            if pos_up<0 :
                direction_list.remove("upward")

            if pos_right<0 :
                direction_list.remove("rightward")

            if pos_left<0 :
                direction_list.remove("leftward")

            if pos_down<0 :
                direction_list.remove("downward")


            current_opposite_direction = utilities.opposite_direction(shadow.direction)

            if utilities.is_in(current_opposite_direction,direction_list):
                direction_list.remove(current_opposite_direction)

            shadow.direction = direction_list[rd.randint(0,len(direction_list)-1)]

            direction_list = ["rightward","upward","leftward","downward"]

        shadow.config_mvmt(shadow.direction)
        shadow.move()

        # 1st Management of player movements

        player.n_mouth += 1
        player.n_mouth = player.n_mouth%8


        precedent_player_direction = player.direction

        if player.next_direction_choosed :

            player.direction = player.next_direction_choice

        else :

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
                        player.direction = "upward"

                    if event.key == pygame.K_DOWN :
                        player.direction = "downward"


        player.config_mvmt(player.direction)

        potential_next_index_i_player, potential_next_index_j_player = player.potential_update_of_indexes_and_positions()


        if mat_map[potential_next_index_i_player][potential_next_index_j_player] == -1 :

            player.direction = precedent_player_direction
            player.config_mvmt(player.direction)

            potential_next_index_i_player, potential_next_index_j_player = player.potential_update_of_indexes_and_positions()


        if mat_map[potential_next_index_i_player][potential_next_index_j_player] >= 0 :

            if player.direction != precedent_player_direction :

                player.next_direction_choosed = False

            player.n_pos += player.step_i + player.step_j
            player.move()


            while 0 < abs(player.n_pos) and abs(player.n_pos) < POS_PER_MVMT :

                player.draw(screen)
                shadow.draw(screen)

                font=pygame.font.Font(None, 40)
                text = font.render(str(score),1,(255,255,255))
                screen.blit(text, (SCREEN_WIDTH/2+10,16))

                pygame.display.flip()

                screen.blit(map, (0,0))
                draw_seed()

                player.n_mouth += 1
                player.n_mouth = player.n_mouth%8

                if player.step_i == 0 :

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

                                player.next_direction_choosed = True
                                player.next_direction_choice = "upward"

                            if event.key == pygame.K_DOWN :
                                player.next_direction_choosed = True
                                player.next_direction_choice = "downward"


                if player.step_j == 0 :

                    for event in pygame.event.get():

                        # Condition de sortie

                        if event.type == pygame.QUIT:
                            running = False

                        # Déplacements du pacman en fonction des entrées claviers

                        if event.type == pygame.KEYDOWN :

                            if event.key == pygame.K_LEFT:
                                player.next_direction_choosed = True
                                player.next_direction_choice = "leftward"

                            if event.key == pygame.K_RIGHT :
                                player.next_direction_choosed = True
                                player.next_direction_choice = "rightward"

                            if event.key == pygame.K_UP :
                                player.direction = "upward"

                            if event.key == pygame.K_DOWN :
                                player.direction = "downward"


                player.config_mvmt(player.direction)

                player.move()
                player.n_pos += player.step_i + player.step_j


                shadow.n_pos += 1

                if shadow.n_pos == POS_PER_MVMT :


                    shadow.potential_update_of_indexes_and_positions()

                    pos_up = mat_map[(shadow.index_i-1)%HEIGHT][(shadow.index_j)%WIDTH]
                    pos_right = mat_map[(shadow.index_i)%HEIGHT][(shadow.index_j+1)%WIDTH]
                    pos_left = mat_map[(shadow.index_i)%HEIGHT][(shadow.index_j-1)%WIDTH]
                    pos_down = mat_map[(shadow.index_i+1)%HEIGHT][(shadow.index_j)%WIDTH]


                    if pos_up<0 :
                        direction_list.remove("upward")

                    if pos_right<0 :
                        direction_list.remove("rightward")

                    if pos_left<0 :
                        direction_list.remove("leftward")

                    if pos_down<0 :
                        direction_list.remove("downward")

                    current_opposite_direction = utilities.opposite_direction(shadow.direction)

                    if utilities.is_in(current_opposite_direction,direction_list):
                        direction_list.remove(current_opposite_direction)


                    shadow.direction = direction_list[rd.randint(0,len(direction_list)-1)]

                    direction_list = ["rightward","upward","leftward","downward"]

                shadow.config_mvmt(shadow.direction)
                shadow.move()


            player.potential_update_of_indexes_and_positions()


            if mat_map[player.index_i][player.index_j] != 0 :

                mat_map[player.index_i][player.index_j] *= 0
                score += 1


        player.draw(screen)
        shadow.draw(screen)

        font=pygame.font.Font(None, 40)
        text = font.render(str(score),1,(255,255,255))
        screen.blit(text, (SCREEN_WIDTH/2+10,16))

        pygame.display.flip()

        screen.blit(map, (0,0))
        draw_seed()


if __name__=="__main__":
    main()
