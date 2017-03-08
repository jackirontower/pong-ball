import pygame

class Settings():
    def __init__(self):
        #screen settings
        self.WIDTH = 800 
        self.HEIGHT = 600
        self.bg_color = 25, 175, 10
        self.line_color = 255, 255, 255
        self.title = 'Ball and Paddle'
        
        #ball settings
        self.ball_spdx = 3
        self.ball_spdy = 3
