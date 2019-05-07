mouvements = {  "left" : {  "step_x_mat" : -1,
                            "step_y_mat" : 0,
                            "i_pacmans" : 2
                          } ,

                "right" : { "step_x_mat" : 1,
                            "step_y_mat" : 0,
                            "i_pacmans" : 0
                          } ,


                "up" : {    "step_x_mat" : 0,
                            "step_y_mat" : -1,
                            "i_pacmans" : 1
                       } ,


                "down" : {  "step_x_mat" : 0,
                            "step_y_mat" : 1,
                            "i_pacmans" : 3
                         }

                }

def mvmt_init(direction):
    return(mouvements[direction])
