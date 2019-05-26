import pygame
import time as t

import classes
import functions
import map


def main() :

    pygame.init()
    running = True

    # Display of the icon, the title ...

    logo = pygame.image.load("images/pacman10.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pacman")


    # Creation of the screen game and initialization of the background

    SCREEN_WIDTH = 606
    SCREEN_HEIGHT = 775

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    map_org = pygame.image.load("images/map.png")
    image_map = pygame.transform.scale(map_org,[SCREEN_WIDTH,SCREEN_HEIGHT])


    # Creation de l'image game over

    black_block_org = pygame.image.load("images/black_block.png")
    image_black_block = pygame.transform.scale(black_block_org,[map.THICK,map.THICK])
    game_over_org = pygame.image.load("images/game_over.png")
    image_game_over = pygame.transform.scale(game_over_org,[SCREEN_WIDTH,SCREEN_WIDTH])

    # Création des images propres au pacman
    # La matrice images_pacman contient toutes les formes de la tête du pacman possibles (différentes formes de bouche et différentes inclinaisons)

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

    image_Shadow_org = pygame.image.load("images/Shadow.png")
    image_Shadow = pygame.transform.scale(image_Shadow_org,[GHOSTS_SIZE,GHOSTS_SIZE])

    image_Speedy_org = pygame.image.load("images/Speedy.png")
    image_Speedy = pygame.transform.scale(image_Speedy_org,[GHOSTS_SIZE,GHOSTS_SIZE])

    image_Pokey_org = pygame.image.load("images/Pokey.png")
    image_Pokey = pygame.transform.scale(image_Pokey_org,[GHOSTS_SIZE,GHOSTS_SIZE])

    image_Bashful_org = pygame.image.load("images/Bashful.png")
    image_Bashful = pygame.transform.scale(image_Bashful_org,[GHOSTS_SIZE,GHOSTS_SIZE])


    # Création des images des graines

    SEED_SIZE = 10

    seed_px = pygame.image.load("Images/seed.png")
    image_seed = pygame.transform.scale(seed_px,[SEED_SIZE,SEED_SIZE])



    # 1) Initialisation de pacman

    index_j_pacman = 11
    index_i_pacman = 20

    OFFSET_PACMAN_X = 11
    OFFSET_PACMAN_Y = 11

    pos_x = map.mat_pos[index_i_pacman][index_j_pacman][0]
    pos_y = map.mat_pos[index_i_pacman][index_j_pacman][1]

    Player = classes.Pacman(pos_x,pos_y,index_i_pacman,index_j_pacman,"leftward",0,OFFSET_PACMAN_X,OFFSET_PACMAN_Y,images_pacman,0,"None")
    # pacman(self,pos_x , pos_y , index_i , index_j , direction , n_pos , offset_x , offset_y , images , n_mouth , next_direction_choice)



    # 2) Initialisation des fantomes
    # 2.1) Initialisation de Shadow

    index_j_Shadow = 1
    index_i_Shadow = 1

    OFFSET_GHOSTS_X = 10
    OFFSET_GHOSTS_Y = 11

    pos_x_Shadow = map.mat_pos[index_i_Shadow][index_j_Shadow][0]
    pos_y_Shadow = map.mat_pos[index_i_Shadow][index_j_Shadow][1]

    Shadow = classes.Ghost(pos_x_Shadow,pos_y_Shadow,index_i_Shadow,index_j_Shadow,"downward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Shadow",image_Shadow,functions.choose_next_direction_shadow)
    #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction)



    # 2.2) Initialisation de Speedy

    index_j_Speedy = 21
    index_i_Speedy = 1

    OFFSET_GHOSTS_X = 10
    OFFSET_GHOSTS_Y = 11

    pos_x_Speedy = map.mat_pos[index_i_Speedy][index_j_Speedy][0]
    pos_y_Speedy = map.mat_pos[index_i_Speedy][index_j_Speedy][1]

    Speedy = classes.Ghost(pos_x_Speedy,pos_y_Speedy,index_i_Speedy,index_j_Speedy,"leftward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Speedy",image_Speedy,functions.choose_next_direction_speedy)
    #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction)



    # 2.3) Initialisation de Bashful

    index_j_Bashful = 1
    index_i_Bashful = 25

    OFFSET_GHOSTS_X = 10
    OFFSET_GHOSTS_Y = 11

    pos_x_Bashful = map.mat_pos[index_i_Bashful][index_j_Bashful][0]
    pos_y_Bashful = map.mat_pos[index_i_Bashful][index_j_Bashful][1]

    Bashful = classes.Ghost(pos_x_Bashful,pos_y_Bashful,index_i_Bashful,index_j_Bashful,"rightward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Bashful",image_Bashful,functions.choose_next_direction_flee)
    #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction  )



    # 2.4) Initialisation de Pokey

    index_j_Pokey = 21
    index_i_Pokey = 25

    OFFSET_GHOSTS_X = 10
    OFFSET_GHOSTS_Y = 11

    pos_x_Pokey = map.mat_pos[index_i_Pokey][index_j_Pokey][0]
    pos_y_Pokey = map.mat_pos[index_i_Pokey][index_j_Pokey][1]

    Pokey = classes.Ghost(pos_x_Pokey,pos_y_Pokey,index_i_Pokey,index_j_Pokey,"upward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Pokey",image_Pokey,functions.choose_next_direction_pokey)
    #   ghost (  self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction)



    # 3) Initialisation des fruits
    # 3.1) Initialisation des graines

    Seed = classes.Eatable("seed",image_seed,1,1)
    #  Eatable ( self , name , image , points , mat_map_value )



    list_of_eatable = [Seed]

    # Initialisation de la variable qui stocke le score

    score = 0

    # Initialisation des temps

    t0 = t.time()
    period = 0.00000001

    # Initialisation de l'affichage

    event_detected = None
    Name = ""

    while event_detected != "return" :

        event_detected = functions.get_event()
        if functions.is_in(event_detected,["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
            Name += event_detected

        if event_detected == "quit" :
            event_detected = "return"
            running = False

        font=pygame.font.Font(None, 50)
        text_name = font.render("Nickname : " + Name,1,(255,220,0))
        screen.blit(text_name, (10,200))

        font=pygame.font.Font(None, 50)
        text1 = font.render("Please enter your nickname" ,1,(255,220,0))
        text2 = font.render("and press \"enter\" when",1,(255,220,0))
        text3 = font.render("you are ready",1,(255,220,0))
        screen.blit(text1, (60,50))
        screen.blit(text2, (90, 90))
        screen.blit(text3, (170, 130))

        pygame.display.flip()

    # font=pygame.font.Font(None, 50)
    # text_name = font.render("You think you're ready, really ?" + Name,1,(255,220,0))
    # screen.blit(text_name, (10,200))
    # pygame.display.flip()
    #
    # t1 = t.time()
    # while abs(t.time()-t1)<2 :
    #     bla = 0


    screen.blit(image_map, [0,0])
    Player.draw(screen)
    Shadow.draw(screen)
    Pokey.draw(screen)
    Speedy.draw(screen)
    Bashful.draw(screen)
    Seed.draw(screen)

    pygame.display.flip()

    event_detected = None
    while not(functions.is_in(event_detected,["rightward","leftward","upward","downward"])):
        event_detected = functions.get_event()

        font=pygame.font.Font(None, 35)
        text_name = font.render("Hi " + Name + " ! Please press an arrow key to start",1,(255,220,0))
        screen.blit(text_name, (30,16))
        pygame.display.flip()

        if event_detected == "quit" :
            event_detected = "leftward"
            running = False


    Player.direction = event_detected


    while running :


        # Management of ghost movements

        Shadow.n_pos += functions.sum(Shadow.steps())
        if abs(Shadow.n_pos) == map.POS_PER_MVMT :
            Shadow.n_pos = 0
            Shadow.update_of_indexes_and_positions()
            Shadow.choose_next_direction(Shadow,Player)
        Shadow.move()


        Pokey.n_pos += functions.sum(Pokey.steps())
        if abs(Pokey.n_pos) == map.POS_PER_MVMT :
            Pokey.n_pos = 0
            Pokey.update_of_indexes_and_positions()
            Pokey.choose_next_direction(Pokey)
        Pokey.move()

        Speedy.n_pos += functions.sum(Speedy.steps())
        if abs(Speedy.n_pos) == map.POS_PER_MVMT :
            Speedy.n_pos = 0
            Speedy.update_of_indexes_and_positions()
            Speedy.choose_next_direction(Speedy,Player)
        Speedy.move()

        Bashful.n_pos += functions.sum(Bashful.steps())
        if abs(Bashful.n_pos) == map.POS_PER_MVMT :
            Bashful.n_pos = 0
            Bashful.update_of_indexes_and_positions()
            Bashful.choose_next_direction(Bashful,Player)
        Bashful.move()

        # Management of Player movements


        event_detected = functions.get_event()

        if event_detected == "quit" :
            running = False

        if functions.is_in(event_detected,["rightward","upward","leftward","downward"]) :
            Player.next_direction_choice = event_detected


        if functions.is_in(Player.next_direction_choice,Player.allowed_directions()):
            Player.direction = Player.next_direction_choice
            Player.next_direction_choice = "None"


        if functions.is_in(Player.direction,Player.allowed_directions()):
            Player.n_pos += sum(Player.steps())
            Player.n_mouth += 1
            Player.n_mouth = Player.n_mouth%8
            Player.move()


        if abs(Player.n_pos) == map.POS_PER_MVMT :
            Player.update_of_indexes_and_positions()
            Player.n_pos = 0


        if map.mat_map[Player.index_i][Player.index_j] != 0 :

            for Classe in list_of_eatable :
                if Classe.mat_map_value == map.mat_map[Player.index_i][Player.index_j]:
                    score += Classe.points

            map.mat_map[Player.index_i][Player.index_j] *= 0


        screen.blit(image_map, [0,0])
        Seed.draw(screen)

        font=pygame.font.Font(None, 40)
        text_score = font.render("Score : " + str(score),1,(255,220,0))
        screen.blit(text_score, (15,16))

        playing_time = int(10*abs(t.time()-t0))/10.0
        text_time = font.render("Time : " + str(playing_time)+ "s",1,(255,220,0))
        screen.blit(text_time, (420,16))


        Player.draw(screen)
        Shadow.draw(screen)
        Pokey.draw(screen)
        Speedy.draw(screen)
        Bashful.draw(screen)
        pygame.display.flip()


        # Conditions de défaite

        delta_x_shadow = abs(Player.pos_x-Shadow.pos_x)
        delta_y_shadow = abs(Player.pos_y-Shadow.pos_y)
        delta_shadow = delta_x_shadow + delta_y_shadow
        delta_x_pokey = abs(Player.pos_x-Pokey.pos_x)
        delta_y_pokey = abs(Player.pos_y-Pokey.pos_y)
        delta_pokey = delta_x_pokey + delta_y_pokey
        delta_x_speedy = abs(Player.pos_x-Speedy.pos_x)
        delta_y_speedy = abs(Player.pos_y-Speedy.pos_y)
        delta_speedy = delta_x_speedy + delta_y_speedy
        delta_x_bashful = abs(Player.pos_x-Bashful.pos_x)
        delta_y_bashful = abs(Player.pos_y-Bashful.pos_y)
        delta_bashful = delta_x_bashful + delta_y_bashful

        if min(delta_shadow,delta_pokey,delta_speedy,delta_bashful)<=map.STEP:

            running = False

            # t1 = t.time()       # Pour réguler la vitesse d'affichage des blocks
            # while abs(t.time()-t1)<3:
    screen.blit(image_game_over,[0,100])
    pygame.display.flip()
    event_detected = None
    while functions.get_event() != "quit":
        Wait = True

            #pygame.display.flip()
            # t1 = t.time()       # Pour réguler la vitesse d'affichage des blocks
            # while abs(t.time()-t1)<3:
            #     wait = True



        # if running == False :
        #


            # for i in range(map.HEIGHT) :
            #     for j in range(map.WIDTH) :
            #         a=0
            #         screen.blit(image_black_block,[map.mat_pos[i][j][0],map.mat_pos[i][j][1]])
            # t1 = t.time()       # Pour réguler la vitesse d'affichage des blocks
            # while abs(t.time()-t1)<3:
            #     wait = True

            #pygame.display.flip()

            # t1 = t.time()       # Pour réguler la vitesse d'affichage des blocks
            # while abs(t.time()-t1)<3:
            #     wait = True
            #
            # screen.blit(image_game_over,[0,100])
            # pygame.display.flip()

            # while running :
            #
            #     event_detected = functions.get_event()
            #     if event_detected == "quit" :
            #         running = False
            # running = False

        # régulation de la vitesse de rafraichissement du jeu

        t1 = t.time()
        while abs(t.time()-t1)<period :
            wait = True

if __name__=="__main__":
    main()
