# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("/home/d/deronzier/Téléchargements/ecole_large.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,600))
     
    # define a variable to control the main loop
    running = True
    
    # background
    Thierry_bernard = pygame.image.load("/home/d/deronzier/Téléchargements/tb.gif")
    bgd_image = pygame.transform.scale(Thierry_bernard,[800,600])
    screen.blit(bgd_image, (0,0))

    # faire apparaitre une image sur l'écran
    image = pygame.image.load("/home/d/deronzier/Téléchargements/pacman.jpg")
    screen.blit(image, (50,50))
    pygame.display.flip()

    # transparance
    image.set_colorkey((255,255,255))
    image.set_alpha(200)

    test = True

    while test :
	    # mouvement
	    # define the position of the smiley
	    xpos = 50
	    ypos = 50
	    # how many pixels we move our smiley each frame
	    step_x = 10
	    step_y = 10
	    # check if the smiley is still on screen, if not change direction
	    screen_width, screen_height = 800, 600
	    #if xpos>screen_width-64 or xpos<0:
	   # 	step_x = -step_x
	   # if ypos>screen_height-64 or ypos<0:
	   # 	step_y = -step_y
	    # update the position of the smiley
	    xpos += step_x # move it to the right
	    ypos += step_y # move it down
	    # now blit the smiley on screen
	    screen.blit(image, (xpos, ypos))
	    # and update the screen (don't forget that!)
	    pygame.display.flip()

	    # first erase the screen 
	    #(just blit the background over anything on screen)
	    #screen.blit(bgd_image, (0,0))
	    # now blit the smiley on screen
	    #screen.blit(image, (xpos, ypos))
	    # and update the screen (don't forget that!)
	    #pygame.display.flip()
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
