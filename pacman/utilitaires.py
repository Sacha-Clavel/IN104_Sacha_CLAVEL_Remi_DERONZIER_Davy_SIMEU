mouvements = {  "left" : {  "step_x" : -1,
                            "step_y" : 0,
                            "i_pacmans" : 2
                          } ,

                "right" : { "step_x" : 1,
                            "step_y" : 0,
                            "i_pacmans" : 0
                          } ,


                "up" : {    "step_x" : 0,
                            "step_y" : -1,
                            "i_pacmans" : 1
                       } ,


                "down" : {  "step_x" : 0,
                            "step_y" : 1,
                            "i_pacmans" : 3
                         }

                }

def mvmt_init(directon):
    return(mouvements[direction])
