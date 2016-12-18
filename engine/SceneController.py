import pygame
import sys
import functools
from Window import *
from Control import *
from ImageControl import *
from stages.Menu import *
from stages.Options import *
from Fonts import *
from Sound import *
from ObjectsLoaded import *


class SceneController:
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.sound = Sound()
        self.fonts = Fonts()
        self.menu()

    def menu(self):
        self.scene = Menu(self.window, self.sound)
        self.scene.update()
        self.scene = AbstractStage(self.window, self.sound, self.fonts)
        self.game()

    def game(self):
        a = self.scene.update()

        if a == "Menu":
            self.menu()
        else:
            if a == "Fase1":
                self.scene = AbstractStage(self.window, self.sound, self.fonts)
            
            elif a == "gameover":
                self.scene.gameover()
            elif a == "parabens1":
                self.scene.parabens1()
            elif a == "Fase2":
                self.scene.fase2()
            self.game()
