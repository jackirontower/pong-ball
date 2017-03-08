# import library
import pygame

# create a class for the ball
class Ball():
    def __init__(self, screen, settings):
		# define variables used by this class
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        
        self.image = pygame.image.load('ball.png').convert()
        self.rect = self.image.get_rect()
        
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.center = float(self.rect.centerx)
        
        self.speedx = settings.ball_spdx
        self.speedy = settings.ball_spdy
        
	# function that updates the ball
    def update(self):
        self.rect.top += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.left < 0 or self.rect.right > self.settings.WIDTH:
            self.speedx = -self.speedx
        if self.rect.top < 0 or self.rect.bottom > self.settings.HEIGHT:
            self.speedy = -self.speedy
            
	# draw the ball on the display
    def blitme(self):
        self.screen.blit(self.image, self.rect)
