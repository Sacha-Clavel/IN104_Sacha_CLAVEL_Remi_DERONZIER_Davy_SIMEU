mouvements = {  "leftward" : {  "step_x_mat" : -1,
                            "step_y_mat" : 0,
                            "i_pacmans" : 2
                          } ,

                "rightward" : { "step_x_mat" : 1,
                            "step_y_mat" : 0,
                            "i_pacmans" : 0
                          } ,


                "upward" : {    "step_x_mat" : 0,
                            "step_y_mat" : -1,
                            "i_pacmans" : 1
                       } ,


                "downward" : {  "step_x_mat" : 0,
                            "step_y_mat" : 1,
                            "i_pacmans" : 3
                         }

                }


def mvmt_init(direction):
    return(mouvements[direction])


# --- GLOBAL PARAMETERS ---

direction_list = ["rightward", "upward", "leftward", "downward"]

STEP = 3
pos_per_mvmt = 9




class Charracter :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos):
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
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.index_i = index_i
        self.index_j = index_j

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




class pacman(Charracter) :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,images,n_mouth) :
        """
            • images : matrix containing all the possible shapes of pacman's head
            ---> NB : in the same column the images of the pacman's head have the same orientation

            • n_mouth : this index corresponds to the numerous of pacman's mouth intermediary position
        """
        Charracter.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos)
        self.images = images
        self.n_mouth = n_mouth


    def draw(self,screen):
        global direction_list
        direction_index = direction_list.index(self.direction)
        images = self.images
        current_image = images[direction_index][self.n_mouth]

        screen.blit(current_image , [self.pos_x,self.pos_y])


    def potential_update_of_indexes(self):
        global pos_per_mvmt

        potential_next_index_i = self.index_i + self.step_i
        potential_next_index_j = self.index_j + self.step_j

        if abs(self.n_pos) == pos_per_mvmt :
            self.index_i = potential_next_index_i
            self.index_j = potential_next_index_j

        return(potential_next_index_i,potential_next_index_j)


class ghost(Charracter):

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,name,image) :
        """
            • name : Name of one of the 4 ghosts

            • image : image that correspond to the ghost named self.name
        """
        Charracter.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos)
        self.image = image
        self.name = name

    def update_indexes(self):

        self.index_i += self.step_i
        self.index_j += self.step_j


    def draw(self,screen):
        pos_x = self.pos_x
        pos_y = self.pos_y

        image = self.image

        screen.blit(image , [pos_x,pos_y])
