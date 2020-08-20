import pygame
from pygame import *

class OneLives():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Instructions")
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Mario Live 1.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.timer = pygame.time.Clock()
		self.start_ticks=pygame.time.get_ticks()



	def Run(self):
		self.Stop=False
		while self.Stop==False:
			self.timer.tick(120)
			self.seconds=((pygame.time.get_ticks()-self.start_ticks)/1000)
			if self.seconds>5:
				self.Stop=True
			self.screen.blit(self.background,(0,0))
			pygame.display.update()
		pygame.quit()



class TwoLives():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Instructions")
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Mario Live 2.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.timer = pygame.time.Clock()
		self.start_ticks=pygame.time.get_ticks()



	def Run(self):
		self.Stop=False
		while self.Stop==False:
			self.timer.tick(120)
			self.seconds=((pygame.time.get_ticks()-self.start_ticks)/1000)
			if self.seconds>5:
				self.Stop=True
			self.screen.blit(self.background,(0,0))
			pygame.display.update()
		pygame.quit()


class ThreeLives():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Instructions")
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Mario Live 3.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.timer = pygame.time.Clock()
		self.start_ticks=pygame.time.get_ticks()



	def Run(self):
		self.Stop=False
		while self.Stop==False:
			self.timer.tick(120)
			self.seconds=((pygame.time.get_ticks()-self.start_ticks)/1000)
			if self.seconds>5:
				self.Stop=True
			self.screen.blit(self.background,(0,0))
			pygame.display.update()
		pygame.quit()
