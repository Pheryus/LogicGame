# Feito por Vinicius Dreifke
import pygame
from ImageControl import *


class Physics2:
    def __init__(self):
        self.gravity = 22
        #self.gravity = ImageControl.defineY(20, True)
        self.vel_x = self.vel_y = self.vel_y_i = 0
        self.fall = False
        self.time = None
        self.on_air = True
        self.jumpable = False
        self.jump_power = 12
        #self.jump_power = ImageControl.defineY(9, True)

    def collision(self):
        self.fall = False
        self.on_air = False
        self.jumpable = True
        self.vel_y = 0
        self.vel_y_i = 0

    def check_falling(self):
        if self.vel_y <= 0:
            self.fall = True
        else:
            self.fall = False

    def update_physics(self, fps):
        if self.fall:
            time = pygame.time.get_ticks()
            if not self.time:
                self.time = time
            self.vel_y = self.gravity * ((time - self.time) / 1000.0) + self.vel_y_i
            #self.vel_y = ImageControl.defineY(self.vel_y, True)
        else:
            self.time = None
            self.vel_y = self.vel_y_i = 0

    def check_falling2(self, player, object):
        player.rect.move_ip((0, 1))
        collisions = pygame.sprite.spritecollide(player, object, False)
        collidable = pygame.sprite.collide_mask
        if not pygame.sprite.spritecollideany(player, collisions, collidable):
            self.fall = True
        player.rect.move_ip((0, -1))

    def get_position(self, player, object):
        if not self.fall:
            self.check_falling2(player, object)
        else:
            self.fall = self.check_collisions((0, self.vel_y), 1, object, player)
        if self.vel_x:
            self.check_collisions((self.vel_x, 0), 0, object, player)

    def jump(self):
        if not self.fall:
            self.vel_y = -self.jump_power
            self.vel_y_i = -self.jump_power
            #self.vel_y = ImageControl.defineY(-self.jump_power, True)
            #self.vel_y_i = ImageControl.defineY(-self.jump_power, True)
            self.on_air = True
            self.fall = True

    def check_collisions(self, offset, index, object, player):
        unaltered = True
        player.rect.move_ip(offset)

        while pygame.sprite.spritecollideany(player, object):
            player.rect[index] += (1 if offset[index] < 0 else -1)
            unaltered = False
        return unaltered
