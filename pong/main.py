# I created this to show you how to move stuff around in pygame.
# Feel free to modify and change whatever you want

# import modules
import pygame
import sys
from settings import Settings
from ball import Ball

# initiate pygame
pygame.init()

def game():
	# use settings.py and create the display and set the title
    settings = Settings()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption(settings.title)
    
	# initalize the ball
    ball = Ball(screen, settings)
    
	# forever move the ball
    while 1:
		# check if user has quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        pygame.draw.line(screen, settings.line_color, (400, 0), (400, 600), 10)
		# draw the ball where it is
        ball.blitme()
        ball.update()
		# update the screen
        pygame.display.flip()
        screen.fill(settings.bg_color)
        
game()
