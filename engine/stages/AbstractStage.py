
#coding: utf-8
from pygame import *
from pygame.locals import *
from ImageControl import *

from BackgroundImage import *
from Enemy import *
from Entity import *
import sys


class AbstractStage:
	def __init__(self, window, sound, fonts):
		self.window = window
		self.sound = sound
		self.fonts = fonts
		self.objects = pygame.sprite.Group()
		self.changeResolution = False
		self.entities = pygame.sprite.Group()
		self.nextStageKey = "Fase1"
		self.actualStageKey = "Fase1"
		self.lastTime = pygame.time.get_ticks()
		self.mouse_position = (0,0)
		self.level = BackgroundImage("Fase1", "mona", "jpg")
		self.level.addImages([["msg1"]])
		self.level.imgs[0].rect.x = 800
		self.level.imgs[0].rect.y = 100
		self.secretappears = False
		self.msgs = None
		#		self.mouse_img = pygame.image.load("../graphics/mouse.jpg").convert_alpha()

	def collision(self, pos):

		for i in self.level.imgs:
			rect = i.rect
			print("entrou aqui")
			if rect.collidepoint(pos):
				mask = pygame.mask.from_surface(i.image)
				offset = pos[0] - rect.x, pos[1] - rect.y

				if mask.get_at(offset):
					if i.collision == "returnStage1":
						self.nextStageKey = "Menu"
						return

		rect = self.level.rect
		if rect.collidepoint(pos) and self.level.mask:
			print("entrou")
			offset = pos[0] - rect.x, pos[1] - rect.y
			if self.level.mask.get_at(offset):

				if self.actualStageKey == "Fase1":
					self.nextStageKey = "parabens1"
				elif self.actualStageKey == "parabens1":

					self.nextStageKey = "Fase2"
			else:
				self.nextStageKey = "gameover"
		"""
		rect = Rect(608,314,240,160)
		if rect.collidepoint(pos) and self.level.mask2:
			offset = pos[0] - rect.x, pos[1] - rect.y
			if self.level.mask.get_at(offset):
				self.secretappears = True
			else:
				self.secretappears = False
		else:
			self.secretappears = False
		"""

	def gameover(self):
		self.level = BackgroundImage("GameOver", "death", "jpg")
		self.level.addImages([["recomeçar", 15, "blink", "returnStage1"], ["voceperdeu"]])


	def parabens1(self):
		self.level = BackgroundImage("Parabens", "Parabens", "jpg")

	def fase2(self):
		self.level = BackgroundImage("Fase2", "esqueleto", "png")
		self.level.addGIF([["ondas.gif", (600, 300)]])
		self.msgs = ["Frequencia", (500, 600)]

	def scene_imgs(self):

		if self.level.background:
			self.window.windowScreen.blit(self.level.background, (0,0))

		self.window.windowScreen.blit(self.level.image, (0,0))

		for i in self.level.imgs:
			if i.appears:
				self.window.windowScreen.blit(i.image, (i.rect.x, i.rect.y))

		for i in self.level.gifs:
			i.gif.render(self.window.windowScreen, (i.x, i.y))

		if self.msgs and self.secretappears:
			text = self.font.fonts["Font1"].render(self.msgs[0], True, (255,255,255))
			self.window.windowScreen.blit(text, self.msgs[1])


	def update(self):
		while (self.actualStageKey == self.nextStageKey):
			self.window.windowScreen.fill((255, 255, 255))
			
			self.scene_imgs()
			self.checkPressed()
			pygame.display.flip()
			self.window.windowScreen.fill((255, 255, 255))
			pygame.time.Clock().tick(60)
			self.level.increaseframecount()
		self.actualStageKey = self.nextStageKey
		return self.nextStageKey


	def checkPressed(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.collision(pygame.mouse.get_pos())
