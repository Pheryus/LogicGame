import pygame
from pygame import *
from ImageControl import *
from GIFImage import *
import os.path

	
class MyImage(pygame.sprite.Sprite):

	def __init__(self, stage, params):
		#, frame, whathappens, collision
		self.appears = True
		self.image = pygame.image.load(stage + params[0]+".png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		try:
			self.frame = params[1]
			self.actualframe = 0
			self.appears = False
		except IndexError:
			self.frame = -1

		try:
			self.whathappens = params[2]
		except IndexError:
			self.whathappens = ""

		try:
			self.collision = params[3]
		except IndexError:
			self.collision = ""


class GIFReference():

	def __init__(self, gif, stage, pos):
		self.x = pos[0]
		self.y = pos[1]
		script_dir = os.path.dirname(os.path.abspath(__file__))
		self.gif = GIFImage(os.path.join(script_dir, stage + gif))


class BackgroundImage(pygame.sprite.Sprite):

	def __init__(self, stage, img, ext):
		pygame.sprite.Sprite.__init__(self)
		self.stage = "../graphics/" + stage + "/"
		self.image = pygame.image.load(self.stage + img + "." + ext).convert_alpha()

		if os.path.exists(self.stage + "mask.png"):
			self.maskimage = pygame.image.load("../graphics/" + stage + "/mask.png").convert_alpha()
			self.mask = pygame.mask.from_surface(self.maskimage)
		else:
			self.maskimage = None
			self.mask = None

		if os.path.exists(self.stage + "background.png"):
			self.backgrund = pygame.image.load("../graphics/" + stage + "/background.png").convert_alpha()
		else:
			self.background = None

		if os.path.exists(self.stage + "mask2.png"):
			self.mask2image = pygame.image.load("../graphics/" + stage + "/mask2.png").convert_alpha()
			self.mask2 = pygame.mask.from_surface(self.mask2image)
		else:
			self.mask2image = None
			self.mask2 = None

		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.imgs = []
		self.gifs = []


	def increaseframecount(self):
		for i in self.imgs:
			if i.frame >= 0:
				i.actualframe += 1
				if i.actualframe == i.frame:
					i.actualframe = 0
					if i.whathappens == "blink":
						i.appears  = not i.appears

	def addImages(self, imgs):
		for i in imgs:
			self.imgs.append(MyImage(self.stage, i))

	def addGIF(self, gifs):
		for i in gifs:
			self.gifs.append(GIFReference(i[0], self.stage, i[1]))