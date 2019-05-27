import map
import functions

# Definition of diverse dictionnaries

directions =    {
                    "rightward" :   { "index" : 0,
                                      "step_i" : 0,
                                      "step_j" : 1
                                    },

                    "upward" :      { "index" : 0,
                                      "step_i" : -1,
                                      "step_j" : 0
                                    },

                    "leftward" :    { "index" : 0,
                                      "step_i" : 0,
                                      "step_j" : -1
                                    },

                    "downward" :    { "index" : 0,
                                      "step_i" : 1,
                                      "step_j" : 0
                                    }
                }

# Definition of diverse classes

class Character :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y):
        """
            • pos_x / pos_y : values of Character's position on the screen (= pixel number)
            ---> NB : these numbers are lower than the width and the height of the screen

            • index_i / index_j : values of Character's "position" in the matrix that represents the map
            ---> NB :   index_i and pos_y are linked
                        index_j and pos_x are linked

            • step_i / step_j : these steps define the movement of the Character
            ---> example :  if the Character's current movement is "going upward"
                                step_i = -1
                                step_j = 0

            • direction : define the current Character's direction
            ---> NB : direction and step_i / step_j are linked
            ---> NB : direction can take 4 string values "rightward", "upward", "leftward", "downward"

            • n_pos : numerous of the Character's intermediary postion (between 2 positions that corresponds to 2 matrix cells)
            ---> NB : this number is lower than the total of intermediary positions reachable by a Character

            • offset_x / offset_y : are linked to the Character's image, they enable the Character's image to perfectly fit with the map
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

        if direction == "None" :
            step_i = 0
            step_j = 0

        return(step_i,step_j)


    def move(self):

        step_i , step_j = Character.steps(self)
        self.pos_x += step_j * map.STEP
        self.pos_y += step_i * map.STEP


    def update_of_indexes_and_positions(self):


        step_i , step_j = Character.steps(self)
        next_index_i = (self.index_i + step_i)%map.HEIGHT
        next_index_j = (self.index_j + step_j)%map.WIDTH

        self.index_i = next_index_i
        self.index_j = next_index_j
        self.pos_x = map.mat_pos[self.index_i][self.index_j][0]
        self.pos_y = map.mat_pos[self.index_i][self.index_j][1]



    def allowed_directions(self):

        if self.n_pos != 0 :
            if self.direction == "rightward" or self.direction == "leftward" :
                directions = ["rightward","leftward"]

            if self.direction == "upward" or self.direction == "downward" :
                directions = ["upward","downward"]

        else :

            directions = functions.allowed_directions_cell(self.index_i,self.index_j)

        return(directions)



class Pacman(Character) :

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y,images,n_mouth,next_direction_choice) :
        """
            • images : matrix containing all the possible shapes of pacman's head
            ---> NB : in the same column the images of the pacman's head have the same orientation

            • n_mouth : this index corresponds to the numerous of pacman's mouth intermediary position

            • next_direction_choice : choice that the player has made for the next possibility of movement
            ---> NB : next_direction_choice can take the 4 possible direction values (= "rightward", "upward, "leftward", "downward")

            • next_direction_choosed : indicates if the player has made a choice for the next direction or not
            ---> NB : next_direction_choosed is a boolean

        """
        Character.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y)
        self.images = images
        self.n_mouth = n_mouth
        self.next_direction_choice = next_direction_choice


    def draw(self,screen):

        direction_list = ["rightward", "upward", "leftward", "downward"]

        direction_index = direction_list.index(self.direction)
        images = self.images
        current_image = images[direction_index][self.n_mouth]

        pos_x = self.pos_x - self.offset_x
        pos_y = self.pos_y - self.offset_y


        screen.blit(current_image , [pos_x , pos_y])




class Ghost(Character):

    def __init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y,name,image,choose_next_direction,is_eaten) :
        """
            • name : Name of one of the 4 ghosts (shadow, speedy, pookey, bashful)

            • image : image that correspond to the ghost named self.name

            • choose_next_direction : is a function, that is unique for each ghost and Characterize how it choose its next direction
        """
        Character.__init__(self,pos_x,pos_y,index_i,index_j,direction,n_pos,offset_x,offset_y)
        self.name = name
        self.image = image
        self.choose_next_direction = choose_next_direction
        self.is_eaten = is_eaten



    def draw(self,screen):
        pos_x = self.pos_x - self.offset_x
        pos_y = self.pos_y - self.offset_y

        image = self.image

        screen.blit(image , [pos_x ,pos_y])



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


    def draw(self,screen):
        mat_map_value = self.mat_map_value
        image = self.image

        for i in range(map.HEIGHT) :
            for j in range(map.WIDTH) :

                if map.mat_map[i][j] == mat_map_value :
                    pos_x = map.mat_pos[i][j][0]
                    pos_y = map.mat_pos[i][j][1]
                    screen.blit(image, (pos_x,pos_y))
