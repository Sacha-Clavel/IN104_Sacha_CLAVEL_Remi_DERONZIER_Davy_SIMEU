import random as rd
import math as m
import map
import classes

import pygame
pygame.init()


def is_in(x,list):
    for i in range(len(list)):
        if x==list[i]:
            return(True)
    return(False)


def sum(list):
    sum = 0
    for elt in list:
        sum += elt
    return(sum)


def opposite_direction(direction):
    if direction == "rightward":
        return("leftward")
    if direction == "leftward":
        return("rightward")
    if direction == "upward":
        return("downward")
    if direction == "downward":
        return("upward")
    return(None)

def allowed_directions_cell(index_i_cell,index_j_cell):
    directions = []

    cell_right = map.mat_map[index_i_cell][(index_j_cell+1)%map.WIDTH]
    cell_up = map.mat_map[(index_i_cell-1)%map.HEIGHT][index_j_cell]
    cell_left = map.mat_map[index_i_cell][(index_j_cell-1)%map.WIDTH]
    cell_down = map.mat_map[(index_i_cell+1)%map.HEIGHT][index_j_cell]

    if cell_right >= 0 :
        directions.append("rightward")

    if cell_up >= 0 :
        directions.append("upward")

    if cell_left >= 0 :
        directions.append("leftward")

    if cell_down >= 0 :
        directions.append("downward")

    return(directions)




def get_event():

    event_detected = "None"

    for event in pygame.event.get():

        # Condition de sortie

        if event.type == pygame.QUIT:
            event_detected = "quit"

            # Déplacements du pacman en fonction des entrées claviers

        if event.type == pygame.KEYDOWN :

            if event.key == pygame.K_LEFT:
                event_detected = "leftward"

            elif event.key == pygame.K_RIGHT :
                event_detected = "rightward"

            elif event.key == pygame.K_UP :
                event_detected = "upward"

            elif event.key == pygame.K_DOWN :
                event_detected = "downward"

            elif event.key == pygame.K_a :
                event_detected = "A"

            elif event.key == pygame.K_b :
                event_detected = "B"

            elif event.key == pygame.K_c :
                event_detected = "C"

            elif event.key == pygame.K_d :
                event_detected = "D"

            elif event.key == pygame.K_e :
                event_detected = "E"

            elif event.key == pygame.K_f :
                event_detected = "F"

            elif event.key == pygame.K_g :
                event_detected = "G"

            elif event.key == pygame.K_h :
                event_detected = "H"

            elif event.key == pygame.K_i :
                event_detected = "I"

            elif event.key == pygame.K_j :
                event_detected = "J"

            elif event.key == pygame.K_k :
                event_detected = "K"

            elif event.key == pygame.K_l :
                event_detected = "L"

            elif event.key == pygame.K_m :
                event_detected = "M"

            elif event.key == pygame.K_n :
                event_detected = "N"

            elif event.key == pygame.K_o :
                event_detected = "O"

            elif event.key == pygame.K_p :
                event_detected = "P"

            elif event.key == pygame.K_q :
                event_detected = "Q"

            elif event.key == pygame.K_r :
                event_detected = "R"

            elif event.key == pygame.K_s :
                event_detected = "S"

            elif event.key == pygame.K_t :
                event_detected = "T"

            elif event.key == pygame.K_u :
                event_detected = "U"

            elif event.key == pygame.K_v :
                event_detected = "V"

            elif event.key == pygame.K_w :
                event_detected = "W"

            elif event.key == pygame.K_x :
                event_detected = "X"

            elif event.key == pygame.K_y :
                event_detected = "Y"

            elif event.key == pygame.K_z :
                event_detected = "Z"

            elif event.key == pygame.K_RETURN :
                event_detected = "return"




        return(event_detected)


def choose_next_direction_pokey(Ghost):

    """
        Pokey est bête, ses déplacements sont complètements aléatoires
    """

    allowed_directions = Ghost.allowed_directions()

    current_opposite_direction = opposite_direction(Ghost.direction)
    if is_in(current_opposite_direction,allowed_directions):
        allowed_directions.remove(current_opposite_direction)

    Ghost.direction = allowed_directions[rd.randint(0,len(allowed_directions)-1)]



def choose_next_direction_shadow(Ghost,Pacman):

    """
        Shadow chasse pacman durant toute la partie (il le suit).

    """


    delta_x = Pacman.index_j - Ghost.index_j
    delta_y = Pacman.index_i - Ghost.index_i

    next_direction_choosed = False
    allowed_directions = Ghost.allowed_directions()

    theta = m.atan2(delta_x,delta_y)

    if -m.pi/4 < theta <= m.pi/4 :
        if is_in("downward",allowed_directions):
            Ghost.direction = "downward"
            next_direction_choosed = True
    if m.pi/4 < theta <= 3*m.pi/4 :
        if is_in("rightward",allowed_directions):
            Ghost.direction = "rightward"
            next_direction_choosed = True
    if 3*m.pi/4 < theta or theta <= -3*m.pi/4 :
        if is_in("upward",allowed_directions):
            Ghost.direction = "upward"
            next_direction_choosed = True
    if -3*m.pi/4 < theta <= -m.pi/4 :
        if is_in("leftward",allowed_directions):
            Ghost.direction = "leftward"
            next_direction_choosed = True

    if not(next_direction_choosed):
        current_opposite_direction = opposite_direction(Ghost.direction)
        if is_in(current_opposite_direction,allowed_directions):
            allowed_directions.remove(current_opposite_direction)

        Ghost.direction = allowed_directions[rd.randint(0,len(allowed_directions)-1)] # Par défaut on prend ee une direction aléatoire

def choose_next_direction_flee(Ghost,Pacman):


    """
        Ce comportement est commun à tous les fantome quand Pacman mange une graine spéciale, (les fantomes fuient)
        --> On utilise exactement la même méthode que choose_next_direction_shadow en changeant juste le signe de delta_x et delta_y
    """

    delta_x = -(Pacman.index_j - Ghost.index_j)
    delta_y = -(Pacman.index_i - Ghost.index_i)

    next_direction_choosed = False
    allowed_directions = Ghost.allowed_directions()

    theta = m.atan2(delta_x,delta_y)

    if -m.pi/4 < theta <= m.pi/4 :
        if is_in("downward",allowed_directions):
            Ghost.direction = "downward"
            next_direction_choosed = True
    if m.pi/4 < theta <= 3*m.pi/4 :
        if is_in("rightward",allowed_directions):
            Ghost.direction = "rightward"
            next_direction_choosed = True
    if 3*m.pi/4 < theta or theta <= -3*m.pi/4 :
        if is_in("upward",allowed_directions):
            Ghost.direction = "upward"
            next_direction_choosed = True
    if -3*m.pi/4 < theta <= -m.pi/4 :
        if is_in("leftward",allowed_directions):
            Ghost.direction = "leftward"
            next_direction_choosed = True

    if not(next_direction_choosed):
        current_opposite_direction = opposite_direction(Ghost.direction)
        if is_in(current_opposite_direction,allowed_directions):
            allowed_directions.remove(current_opposite_direction)

        Ghost.direction = allowed_directions[rd.randint(0,len(allowed_directions)-1)] # Par défaut on prend ee une direction aléatoire




def choose_next_direction_speedy(Ghost,Pacman):

    """
        Speedy essaie de bloquer Pacman en anticipant ses déplacements :
        --> Quand pacman entre dans un couloir, on prédit la "case de sortie du couloir" (quand le pacman peut faire un autre mouvement que faire demi-tour)
            et on utilise la même méthode que choose_next_direction_shadow pour que speedy se dirige vers la case trouvée
        --> Si le pacman est immobile ou n'est pas dans un couloir, speedy le chasse comme shadow
    """

    predicted_cell_index_i = Pacman.index_i
    predicted_cell_index_j = Pacman.index_j

    allowed_directions_prediction = allowed_directions_cell(predicted_cell_index_i,predicted_cell_index_j)

    direction_prediction = Pacman.direction
    step_i = classes.directions[direction_prediction]["step_i"]
    step_j = classes.directions[direction_prediction]["step_j"]
    predicted_cell_index_i += step_i
    predicted_cell_index_j += step_j


    if len(allowed_directions_prediction)>2 or map.mat_map[predicted_cell_index_i][predicted_cell_index_j] < 0 :

        choose_next_direction_shadow(Ghost,Pacman)

    else :

        allowed_directions_prediction = allowed_directions_cell(predicted_cell_index_i,predicted_cell_index_j)

        while len(allowed_directions_prediction)<=2 :

            opposite_direction_prediction = opposite_direction(direction_prediction)
            if is_in(opposite_direction_prediction,allowed_directions_prediction):
                allowed_directions_prediction.remove(opposite_direction_prediction)
            direction_prediction = allowed_directions_prediction[0]

            step_i = classes.directions[direction_prediction]["step_i"]
            step_j = classes.directions[direction_prediction]["step_j"]
            predicted_cell_index_i += step_i
            predicted_cell_index_j += step_j

            allowed_directions_prediction = allowed_directions_cell(predicted_cell_index_i,predicted_cell_index_j)


        delta_x = predicted_cell_index_j - Ghost.index_j
        delta_y = predicted_cell_index_i- Ghost.index_i

        next_direction_choosed = False
        allowed_directions = Ghost.allowed_directions()

        theta = m.atan2(delta_x,delta_y)

        if -m.pi/4 < theta <= m.pi/4 :
            if is_in("downward",allowed_directions):
                Ghost.direction = "downward"
                next_direction_choosed = True
        if m.pi/4 < theta <= 3*m.pi/4 :
            if is_in("rightward",allowed_directions):
                Ghost.direction = "rightward"
                next_direction_choosed = True
        if 3*m.pi/4 < theta or theta <= -3*m.pi/4 :
            if is_in("upward",allowed_directions):
                Ghost.direction = "upward"
                next_direction_choosed = True
        if -3*m.pi/4 < theta <= -m.pi/4 :
            if is_in("leftward",allowed_directions):
                Ghost.direction = "leftward"
                next_direction_choosed = True

        if not(next_direction_choosed):
            current_opposite_direction = opposite_direction(Ghost.direction)
            if is_in(current_opposite_direction,allowed_directions):
                allowed_directions.remove(current_opposite_direction)

            Ghost.direction = allowed_directions[rd.randint(0,len(allowed_directions)-1)] # Par défaut on prend une direction aléatoire
