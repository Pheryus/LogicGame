import pygame
from ImageControl import *
from stages.AbstractStage import *


class Menu(AbstractStage):
    def __init__(self,window, sound):
        self.name = "Menu"
        self.window = window
        self.sound = sound
        self.change = False
        self.choiceOptions = ["Stage1", "Options", "Quit"]
        self.choiceKey = 0
        self.loadImages()        
        self.loadSounds()
        self.resizeImages()
        if not pygame.mixer.music.get_busy():
            self.music = pygame.mixer.music.load("../sound/BGM/menu.mp3")
            pygame.mixer.music.play(0)

    def loadImages(self):
        self.menuImage = pygame.image.load("../graphics/Menu.jpg").convert_alpha()
        self.options = [pygame.image.load("../graphics/Menu/opt" + str(i) + ".png").convert_alpha() for i in
                        range(1, 4)]
        self.fixoptions = []
        for i in range(3):
            self.fixoptions.append(self.options[i])

    def loadSounds(self):
        self.sound.soundMenu()

    def resizeImages(self):

        for i in range(0, 3):
            self.fixoptions[i] = self.options[i]
        self.fixoptions[0] = ImageControl.zoomImage(self.options[0], 1.25)

    def scene_imgs(self):
        ImageControl.centerImage(self.window, self.menuImage)
        
        ImageControl.centerImage(self.window, self.fixoptions[0])
        ImageControl.belowcenterImage(self.window, 1, self.fixoptions[1])
        ImageControl.belowcenterImage(self.window, 5, self.fixoptions[2])

    def update(self):
        while True:
            #self.window.windowScreen.fill((255, 255, 255))
            self.scene_imgs()
            pygame.display.flip()
            #self.window.windowScreen.fill((255, 255, 255))

            pygame.time.Clock().tick(15)
            aux = self.menuSelection(self.checkPressed())

            self.checkMouse()

            if self.window.resolutionChange:
                self.fixResolution()
            if aux != "":
                return aux, False, self.change

    def fixResolution(self):
        self.resizeImages()
        self.window.resolutionChange = False
        self.change = True

    def checkMouse(self):
        for i in self.options:



    def checkPressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif event.type == VIDEORESIZE:
                self.window.changeResolution(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "enter"
                elif event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_DOWN:
                    return "down"

    def menuSelection(self, action):

        if not action:
            return ""

        if action == "enter":
            self.sound.playSound("game_start")
            return self.choiceOptions[self.choiceKey]

        if action != "up" and action != "down":
            return ""

        self.fixoptions[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 0.8)

        if action == "up":
            self.sound.playSound("cursor_move")
            self.choiceKey -= 1
            if self.choiceKey < 0:
                self.choiceKey = 2

        elif action == "down":
            self.sound.playSound("cursor_move")
            self.choiceKey = (self.choiceKey + 1) % 3

        self.fixoptions[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 1.25)

        return ""
