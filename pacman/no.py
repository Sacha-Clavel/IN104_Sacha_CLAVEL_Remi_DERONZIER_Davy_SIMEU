def is_in(x,list):
    for i in range(len(list)):
        if x==list[i]:
            return(True)
    return(False)

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


# pygame.init()

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

            if event.key == pygame.K_RIGHT :
                event_detected = "rightward"

            if event.key == pygame.K_UP :
                event_detected = "upward"

            if event.key == pygame.K_DOWN :
                event_detected = "downward"

        return(event_detected)



def choose_next_direction_pokey(Ghost):

    if Ghost.n_pos == POS_PER_MVMT :

        allowed_directions = Ghost.allowed_directions()

        current_opposite_direction = opposite_direction(Ghost.direction)

        if is_in(current_opposite_direction,allowed_directions):
            allowed_directions.remove(current_opposite_direction)

        Ghost.direction = allowed_directions[rd.randint(0,len(allowed_directions)-1)]
