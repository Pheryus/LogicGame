# Feito por Vinicius Dreifke
import pygame
from ImageControl import *


class Physics:
    def __init__(self):
        self.constantgravity = 15
        self.gravity = 15
        self.vel_x = self.vel_y = self.vel_y_i = 0
        self.fall = True
        self.time = None
        self.constantjump_power = 8
        self.jump_power = 8

    def check_falling(self):
        if self.vel_y < 0:
            self.fall = True
        else:
            self.fall = False

    def update_physics(self, fps):
        if self.fall:
            time = pygame.time.get_ticks()
            if not self.time:
                self.time = time
            self.vel_y = self.gravity * ((time - self.time) / 1000.0) + self.vel_y_i
        else:
            self.time = None
            self.vel_y = (self.vel_y + self.vel_y_i) / fps
            self.check_falling()

    def get_position(self):
        if not self.fall:
            self.check_falling()

    def jump(self):
        if self.fall:
            self.vel_y_i = -self.jump_power
            self.vel_y_i = self.vel_y_i
            self.fall = False