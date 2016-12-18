import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.soundVolume = 1.00
        self.soundList = {}

    def str_to_atrib(self, str):
        return functools.reduce(getattr, str.split("."), sys.modules[__name__])

    def playSound(self, soundname):
        track_number = self.soundList[soundname]
        track_number.play()

    def soundMenu(self):
        self.sound_cursor_move = pygame.mixer.Sound("../sound/soundeffect/Menu/cursor_move2.wav")
        self.sound_cursor_back = pygame.mixer.Sound("../sound/soundeffect/Menu/cursor_back2.wav")
        self.sound_game_start = pygame.mixer.Sound("../sound/soundeffect/Menu/game_start2.wav")
        self.soundList["cursor_move"] = self.sound_cursor_move
        self.soundList["cursor_back"] = self.sound_cursor_back
        self.soundList["game_start"] = self.sound_game_start

    def soundStage1(self):
        self.sound_pop = pygame.mixer.Sound("../sound/soundeffect/pop.wav")
        self.soundList["pop"] = self.sound_pop
