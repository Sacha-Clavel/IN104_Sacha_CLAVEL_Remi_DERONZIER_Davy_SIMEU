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
    image_black_background = pygame.transform.scale(black_block_org,[SCREEN_WIDTH,SCREEN_HEIGHT])
    game_over_org = pygame.image.load("images/game_over.png")
    image_game_over = pygame.transform.scale(game_over_org,[550,550])
    you_win_org = pygame.image.load("images/you_win.png")
    image_you_win = pygame.transform.scale(you_win_org,[550,508])

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

    image_Flee_org = pygame.image.load("images/flee.png")
    image_Flee = pygame.transform.scale(image_Flee_org,[GHOSTS_SIZE,GHOSTS_SIZE])



    # Création des images des graines

    SEED_SIZE = 10

    seed_org = pygame.image.load("Images/seed.png")
    image_seed = pygame.transform.scale(seed_org,[SEED_SIZE,SEED_SIZE])

    STAR_SIZE = 15

    star_org = pygame.image.load("Images/star.png")
    image_star = pygame.transform.scale(star_org,[STAR_SIZE,STAR_SIZE])

    # Creation des images des vies

    live_1_org = pygame.image.load("Images/1_live.png")
    image_live_1 = pygame.transform.scale(live_1_org,[31,25])

    live_2_org = pygame.image.load("Images/2_live.png")
    image_live_2 = pygame.transform.scale(live_2_org,[66,25])

    live_3_org = pygame.image.load("Images/3_live.png")
    image_live_3 = pygame.transform.scale(live_3_org,[90,25])

    def characters_initialisation():

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

        Shadow = classes.Ghost(pos_x_Shadow,pos_y_Shadow,index_i_Shadow,index_j_Shadow,"downward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Shadow",image_Shadow,functions.choose_next_direction_shadow,False)
        #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction   ,   is_eaten)



        # 2.2) Initialisation de Speedy

        index_j_Speedy = 21
        index_i_Speedy = 1

        OFFSET_GHOSTS_X = 10
        OFFSET_GHOSTS_Y = 11

        pos_x_Speedy = map.mat_pos[index_i_Speedy][index_j_Speedy][0]
        pos_y_Speedy = map.mat_pos[index_i_Speedy][index_j_Speedy][1]

        Speedy = classes.Ghost(pos_x_Speedy,pos_y_Speedy,index_i_Speedy,index_j_Speedy,"leftward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Speedy",image_Speedy,functions.choose_next_direction_speedy,False)
        #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction   ,   is_eaten)



        # 2.3) Initialisation de Bashful

        index_j_Bashful = 1
        index_i_Bashful = 25

        OFFSET_GHOSTS_X = 10
        OFFSET_GHOSTS_Y = 11

        pos_x_Bashful = map.mat_pos[index_i_Bashful][index_j_Bashful][0]
        pos_y_Bashful = map.mat_pos[index_i_Bashful][index_j_Bashful][1]

        Bashful = classes.Ghost(pos_x_Bashful,pos_y_Bashful,index_i_Bashful,index_j_Bashful,"rightward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Bashful",image_Bashful,functions.choose_next_direction_bashful,False)
        #   ghost   (    self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction   ,   is_eaten)



        # 2.4) Initialisation de Pokey

        index_j_Pokey = 21
        index_i_Pokey = 25

        OFFSET_GHOSTS_X = 10
        OFFSET_GHOSTS_Y = 11

        pos_x_Pokey = map.mat_pos[index_i_Pokey][index_j_Pokey][0]
        pos_y_Pokey = map.mat_pos[index_i_Pokey][index_j_Pokey][1]

        Pokey = classes.Ghost(pos_x_Pokey,pos_y_Pokey,index_i_Pokey,index_j_Pokey,"upward",0,OFFSET_GHOSTS_X,OFFSET_GHOSTS_Y,"Pokey",image_Pokey,functions.choose_next_direction_pokey,False)
        #   ghost (  self   , pos_x   ,   pos_y   ,   index_i   ,   index_j   ,   direction   ,   n_pos   ,   offset_x   ,   offset_y   ,   name   ,   image   ,   choose_next_direction   ,   is_eaten)

        return(Player,Shadow,Pokey,Speedy,Bashful)

    Player, Shadow, Pokey, Speedy, Bashful = characters_initialisation()


    # 3) Initialisation des fruits
    # 3.1) Initialisation des graines

    Seed = classes.Eatable("seed",image_seed,1,1)
    Star = classes.Eatable("star",image_star,1,2)
    #  Eatable ( self , name , image , points , mat_map_value )
    list_of_eatable = [Seed,Star]


    # Premiers affichages, et intéractions avec l'utilisateur

    event_detected = None
    Name = ""

    while event_detected != "return" :

        event_detected = functions.get_event()
        if functions.is_in(event_detected,["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","1","2","3","4","5","6","7","8","9"]):
            Name += event_detected

        if event_detected == "delete" :
            Name = Name[:-1]

        if event_detected == "quit" :
            event_detected = "return"
            running = False


        screen.blit(image_black_background,[0,0])

        font=pygame.font.Font(None, 50)
        text = font.render("Please enter your nickname" ,1,(255,220,0))
        screen.blit(text, (60,50))
        text = font.render("and press \"enter\" when",1,(255,220,0))
        screen.blit(text, (90, 90))
        text = font.render("it's done",1,(255,220,0))
        screen.blit(text, (220, 130))


        text_name = font.render("Nickname : " + Name,1,(255,220,0))
        screen.blit(text_name, (10,230))

        pygame.display.flip()

    text = font.render("Hi "+Name+" !",1,(255,220,0))
    screen.blit(text, (200,330))

    text = font.render("Now, please select the speed ",1,(255,220,0))
    screen.blit(text, (55,370))
    text = font.render("of the game with your keyboard ! ",1,(255,220,0))
    screen.blit(text, (30,410))

    text = font.render("1 : Slow ",1,(255,220,0))
    screen.blit(text, (100,500))

    text = font.render("2 : Medium ",1,(255,220,0))
    screen.blit(text, (100,560))

    text = font.render("3 : Fast, really fast ! ",1,(255,220,0))
    screen.blit(text, (100,620))

    pygame.display.flip()

    event_detected = None
    while not(functions.is_in(event_detected,["1","2","3"])) :
        event_detected = functions.get_event()

        if event_detected == "1":
            period = 0.03

        elif event_detected == "2":
            period = 0.001

        elif event_detected == "3":
            period = 0.00001

        if event_detected == "quit" :
            event_detected = "1"
            running = False



    screen.blit(image_map, [0,0])
    Seed.draw(screen)
    Star.draw(screen)
    Player.draw(screen)
    Shadow.draw(screen)
    Pokey.draw(screen)
    Speedy.draw(screen)
    Bashful.draw(screen)


    pygame.display.flip()

    event_detected = None
    while not(functions.is_in(event_detected,["rightward","leftward","upward","downward"])):
        event_detected = functions.get_event()

        font=pygame.font.Font(None, 35)
        text_name = font.render("Dear " + Name + ", please press an arrow key to start",1,(255,220,0))
        screen.blit(text_name, (30,16))
        pygame.display.flip()

        if event_detected == "quit" :
            event_detected = "leftward"
            running = False


    Player.direction = event_detected
    t0 = t.time()
    flee_time_init = t.time()
    ghosts_are_fleeing = False
    score = 0
    lives = 3

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
            Pokey.choose_next_direction(Pokey,Player)
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

                if map.mat_map[Player.index_i][Player.index_j] == 2 :

                    flee_time_init = t.time()
                    Shadow.image = image_Flee
                    Pokey.image = image_Flee
                    Speedy.image = image_Flee
                    Bashful.image = image_Flee
                    Shadow.choose_next_direction = functions.choose_next_direction_flee
                    Pokey.choose_next_direction = functions.choose_next_direction_flee
                    Speedy.choose_next_direction = functions.choose_next_direction_flee
                    Bashful.choose_next_direction = functions.choose_next_direction_flee
                    ghosts_are_fleeing = True

            map.mat_map[Player.index_i][Player.index_j] *= 0

        if abs(t.time()-flee_time_init)>10 :
                Shadow.image = image_Shadow
                Pokey.image = image_Pokey
                Speedy.image = image_Speedy
                Bashful.image = image_Bashful
                Shadow.choose_next_direction = functions.choose_next_direction_shadow
                Pokey.choose_next_direction = functions.choose_next_direction_pokey
                Speedy.choose_next_direction = functions.choose_next_direction_speedy
                Bashful.choose_next_direction = functions.choose_next_direction_bashful
                ghosts_are_fleeing = False


        screen.blit(image_map, [0,0])
        Seed.draw(screen)
        Star.draw(screen)

        font=pygame.font.Font(None, 40)
        text_score = font.render("Score : " + str(score),1,(255,220,0))
        screen.blit(text_score, (15,16))

        playing_time = int(10*abs(t.time()-t0))/10.0
        text_time = font.render("Time : " + str(playing_time)+ "s",1,(255,220,0))
        screen.blit(text_time, (420,16))

        if lives == 3 :
            screen.blit(image_live_3,[260,14])
        elif lives == 2 :
            screen.blit(image_live_2,[260,14])
        elif lives == 1 :
            screen.blit(image_live_1,[260,14])

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
            if ghosts_are_fleeing :
                if delta_shadow <= map.STEP :
                    Shadow.is_eaten = True

                if delta_speedy <= map.STEP :
                    Speedy.is_eaten = True

                if delta_pokey <= map.STEP :
                    Pokey.is_eaten = True

                if delta_bashful <= map.STEP :
                    Bashful.is_eaten = True


            else :

                lives -=1

                while not(functions.is_in(event_detected,["rightward","leftward","upward","downward"])) and lives>0 :
                    event_detected = functions.get_event()

                    font=pygame.font.Font(None, 35)
                    text_name = font.render("Haha ! Press an arrow key to continue",1,(255,220,0))
                    screen.blit(text_name, (90,380))
                    pygame.display.flip()

                    if event_detected == "quit" :
                        event_detected = "leftward"
                        running = False

                Player, Shadow, Pokey, Speedy, Bashful = characters_initialisation()
                Player.direction = event_detected

        if Shadow.is_eaten :
            Shadow.index_i = 11
            Shadow.index_j = 9
            Shadow.pos_x = map.mat_pos[Shadow.index_i][Shadow.index_j][0]
            Shadow.pos_y = map.mat_pos[Shadow.index_i][Shadow.index_j][1]
            Shadow.choose_next_direction = functions.choose_next_direction_eaten
            Shadow.image = image_Shadow
            Shadow.direction = "None"

        if Speedy.is_eaten :
            Speedy.index_i = 12
            Speedy.index_j = 10
            Speedy.pos_x = map.mat_pos[Speedy.index_i][Speedy.index_j][0]
            Speedy.pos_y = map.mat_pos[Speedy.index_i][Speedy.index_j][1]
            Speedy.choose_next_direction = functions.choose_next_direction_eaten
            Speedy.image = image_Speedy
            Speedy.direction = "None"

        if Pokey.is_eaten :
            Pokey.index_i = 11
            Pokey.index_j = 12
            Pokey.pos_x = map.mat_pos[Pokey.index_i][Pokey.index_j][0]
            Pokey.pos_y = map.mat_pos[Pokey.index_i][Pokey.index_j][1]
            Pokey.choose_next_direction = functions.choose_next_direction_eaten
            Pokey.image = image_Pokey
            Pokey.direction = "None"

        if Bashful.is_eaten :
            Bashful.index_i = 12
            Bashful.index_j = 13
            Bashful.pos_x = map.mat_pos[Bashful.index_i][Bashful.index_j][0]
            Bashful.pos_y = map.mat_pos[Bashful.index_i][Bashful.index_j][1]
            Bashful.choose_next_direction = functions.choose_next_direction_eaten
            Bashful.image = image_Bashful
            Bashful.direction = "None"


        max_map = map.mat_map[0][0]

        for i in range(map.HEIGHT) :
            for j in range(map.WIDTH) :
                if map.mat_map[i][j] > max_map :
                    max_map = map.mat_map[i][j]


        if lives <= 0 or max_map==0 :
            running = False



        t1 = t.time()
        while abs(t.time()-t1)<period :
            wait = True




    screen.blit(image_black_background,[0,0])

    if max_map >0 :
        screen.blit(image_game_over,[30,40])
        font=pygame.font.Font(None, 45)
        text_name = font.render("... Your final score was "+str(score)+" ...",1,(255,220,0))
        screen.blit(text_name, (100,580))
    else :
        screen.blit(image_you_win,[30,40])


    pygame.display.flip()

    event_detected = None

    while functions.get_event() != "quit":
        Wait = True



if __name__=="__main__":
    main()
