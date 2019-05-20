# --- GLOBAL PARAMETERS ---

direction_list = ["rightward", "upward", "leftward", "downward"]



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

OFFSET_PACMAN_X = 11
OFFSET_PACMAN_Y = 11

# --- Useful fonctions ---

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




class Charracter :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y):
        """
            • pos_x / pos_y : values of charracter's position on the screen (= pixel number)
            ---> NB : these numbers are lower than the width and the height of the screen

            • index_i / index_j : values of charracter's "position" in the matrix that represents the map
            ---> NB :   index_i and pos_y are linked
                        index_j and pos_x are linked

            • step_i / step_j : these steps define the movement of the charracter
            ---> example :  if the charracter's current movement is "going upward"
                                step_i = -1
                                step_j = 0

            • direction : define the current charracter's direction
            ---> NB : direction and step_i / step_j are linked
            ---> NB : direction can take 4 string values "rightward", "upward", "leftward", "downward"

            • n_pos : numerous of the charracter's intermediary postion (between 2 positions that corresponds to 2 matrix cells)
            ---> NB : this number is lower than the total of intermediary positions reachable by a charracter

            • offset_x / offset_y : are linked to the charracter's image, they enable the charracter's image to perfectly fit with the map
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.index_i = index_i
        self.index_j = index_j
        self.offset_x = offset_x
        self.offset_y = offset_y

        if direction == "rightward" :
            self.step_i = 0
            self.step_j = 1

        if direction == "upward" :
            self.step_i = -1
            self.step_j = 0

        if direction == "leftward" :
            self.step_i = 0
            self.step_j = -1

        if direction == "downward" :
            self.step_i = 1
            self.step_j = 0
        self.direction = direction
        self.n_pos = n_pos


    def config_mvmt(self,direction):
        self.direction = direction

        if direction == "rightward" :
            self.step_i = 0
            self.step_j = 1

        if direction == "upward" :
            self.step_i = -1
            self.step_j = 0

        if direction == "leftward" :
            self.step_i = 0
            self.step_j = -1

        if direction == "downward" :
            self.step_i = 1
            self.step_j = 0


    def move(self):
        global STEP
        self.pos_x += self.step_j * STEP
        self.pos_y += self.step_i * STEP


    def potential_update_of_indexes_and_positions(self):
        global POS_PER_MVMT
        global mat_pos

        potential_next_index_i = self.index_i + self.step_i
        potential_next_index_j = self.index_j + self.step_j

        if potential_next_index_j >= WIDTH :
            potential_next_index_j = 0

        if potential_next_index_j < 0 :
            potential_next_index_j = WIDTH-1

        if potential_next_index_i >= HEIGHT:
            potential_next_index_i = 0

        if potential_next_index_i < 0:
            potential_next_index_i = HEIGHT-1

        if abs(self.n_pos) == POS_PER_MVMT :

            self.n_pos = 0

            self.index_i = potential_next_index_i
            self.index_j = potential_next_index_j
            self.pos_x = mat_pos[self.index_i][self.index_j][0] - self.offset_x
            self.pos_y = mat_pos[self.index_i][self.index_j][1] - self.offset_y

        return(potential_next_index_i,potential_next_index_j)



class pacman(Charracter) :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y,images,n_mouth,next_direction_choice,next_direction_choosed) :
        """
            • images : matrix containing all the possible shapes of pacman's head
            ---> NB : in the same column the images of the pacman's head have the same orientation

            • n_mouth : this index corresponds to the numerous of pacman's mouth intermediary position

            • next_direction_choice : choice that the player has made for the next possibility of movement
            ---> NB : next_direction_choice can take the 4 possible direction values (= "rightward", "upward, "leftward", "downward")

            • next_direction_choosed : indicates if the player has made a choice for the next direction or not
            ---> NB : next_direction_choosed is a boolean

        """
        Charracter.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y)
        self.images = images
        self.n_mouth = n_mouth
        self.next_direction_choice = next_direction_choice
        self.next_direction_choosed = next_direction_choosed


    def draw(self,screen):
        global direction_list
        direction_index = direction_list.index(self.direction)
        images = self.images
        current_image = images[direction_index][self.n_mouth]

        screen.blit(current_image , [self.pos_x,self.pos_y])
        



class ghost(Charracter):

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y,name,image) :
        """
            • name : Name of one of the 4 ghosts

            • image : image that correspond to the ghost named self.name
        """
        Charracter.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y)
        self.name = name
        self.image = image



    def draw(self,screen):
        pos_x = self.pos_x
        pos_y = self.pos_y

        image = self.image

        screen.blit(image , [pos_x,pos_y])
