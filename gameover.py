import pygame
from pygame import *

class GameOver():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.display.set_caption("Game Over")
		pygame.mixer.music.load('/Users/Zahza/Desktop/Mario 3.0/Audio/210-game-over.wav')
		pygame.mixer.music.play(-1)		
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/GameOver.jpg')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.timer = pygame.time.Clock()
		self.start_ticks=pygame.time.get_ticks()



	def Run(self):
		self.Stop=False
		while self.Stop==False:
			self.timer.tick(120)
			self.seconds=((pygame.time.get_ticks()-self.start_ticks)/1000)
			if self.seconds>10:
				self.Stop=True
			self.screen.blit(self.background,(0,0))
			pygame.display.update()
		pygame.quit()
