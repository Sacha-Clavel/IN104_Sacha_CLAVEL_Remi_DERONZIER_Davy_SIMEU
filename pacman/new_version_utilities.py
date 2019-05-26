# --- GLOBAL PARAMETERS ---

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

# --- Usedfonctions ---

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
        self.direction = direction
        self.n_pos = n_pos
        self.offset_x = offset_x
        self.offset_y = offset_y


    def steps(self):
        direction = self.direction

        if direction == "rightward" :
            step_i = 0
            step_j = 1

        if direction == "upward" :
            step_i = -1
            step_j = 0

        if direction == "leftward" :
            step_i = 0
            step_j = -1

        if direction == "downward" :
            step_i = 1
            step_j = 0

        return(step_i,step_j)


    def move(self, step_i, step_j):
        global STEP

        self.pos_x += step_j * STEP
        self.pos_y += step_i * STEP


    def potential_update_of_indexes_and_positions(self, step_i, step_j):
        global POS_PER_MVMT
        global WIDTH
        global HEIGHT
        global mat_pos

        potential_next_index_i = (self.index_i + step_i)%HEIGHT
        potential_next_index_j = (self.index_j + step_j)%WIDTH

        if abs(self.n_pos) == POS_PER_MVMT :

            self.n_pos = 0
            self.index_i = potential_next_index_i
            self.index_j = potential_next_index_j
            self.pos_x = mat_pos[self.index_i][self.index_j][0] - self.offset_x
            self.pos_y = mat_pos[self.index_i][self.index_j][1] - self.offset_y

        return(potential_next_index_i,potential_next_index_j)


    def allowed_directions(self):
        global HEIGHT
        global WIDTH

        if self.n_pos != 0 :
            if self.direction == "rightward" or self.direction == "leftward" :
                directions = ["rightward","leftward"]

            if self.direction == "upward" or self.direction == "downward" :
                directions = ["upward","downward"]

        else :
            directions = []

            cell_right = mat_map[self.index_i][(self.index_j+1)%WIDTH]
            cell_up = mat_map[(self.index_i-1)%HEIGHT][self.index_j]
            cell_left = mat_map[self.index_i][(self.index_j-1)%WIDTH]
            cell_down = mat_map[(self.index_i+1)%HEIGHT][self.index_j]

            if cell_right >= 0 :
                directions.append("rightward")

            if cell_up >= 0 :
                directions.append("upward")

            if cell_left >= 0 :
                directions.append("leftward")

            if cell_down >= 0 :
                directions.append("downward")

        return(directions)



class Pacman(Charracter) :

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

        direction_list = ["rightward", "upward", "leftward", "downward"]

        direction_index = direction_list.index(self.direction)
        images = self.images
        current_image = images[direction_index][self.n_mouth]

        screen.blit(current_image , [self.pos_x,self.pos_y])




class Ghost(Charracter):

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y,name,image,choose_next_direction) :
        """
            • name : Name of one of the 4 ghosts (shadow, speedy, pookey, bashful)

            • image : image that correspond to the ghost named self.name

            • choose_next_direction : is a function, that is unique for each ghost and charracterize how it choose its next direction
        """
        Charracter.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y)
        self.name = name
        self.image = image
        self.choose_next_direction = choose_next_direction



    def draw(self,screen):
        pos_x = self.pos_x
        pos_y = self.pos_y

        image = self.image

        screen.blit(image , [pos_x,pos_y])



class Eatable :

    def __init__(self,name,image,points,mat_map_value):
        """
            • name : name of the object eatable by pacman (seed, cherry, banana ...)

            • image : image of the Eatable

            • points : points added to the score when pacman eats the Eatable
        """
        self.name = name
        self. image = image
        self.points = points
        self.mat_map_value = mat_map_value


    def draw(self):
        mat_map_value = self.mat_map_value
        image = self.image

        for i in range(len(mat_map)) :
            for j in range(len(mat_map[i])) :

                if mat_map[i][j] == mat_map_value :
                    pos_x = mat_pos[i][j][0]
                    pos_y = mat_pos[i][j][1]
                    screen.blit(image, (pos_x,pos_y))
