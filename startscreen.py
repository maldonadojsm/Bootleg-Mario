import pygame
from pygame import *

class StartScreen():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.display.set_caption("Bootleg Mario!")
		#pygame.mixer.music.load('/Users/Zahza/Desktop/StayAlert_.wav')
		#pygame.mixer.music.play(-1)
		x=0
		y=0
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Black Background.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.mario_logo=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Mario Logo.png')
		self.mario_logo=transform.scale(self.mario_logo,(600,200))
		self.start_icon=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/start-game-button.png')
		#self.start_icon=transform.scale(self.start_icon,())		
		self.start_icon_rect=pygame.Rect((170,450),(460,85))

	def Run(self):
		self.Stop=False
		while self.Stop==False:
			#Add song
			self.Event()
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.mario_logo,(100,50))
			self.screen.blit(self.start_icon,(170,450))
			pygame.display.update()
		pygame.quit()		

	def Event(self):		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				self.Stop=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					self.Stop=True
			if event.type==pygame.MOUSEBUTTONDOWN:
				x,y=pygame.mouse.get_pos()
				self.mouserect=pygame.Rect((x,y),(1,1))
				if self.mouserect.colliderect(self.start_icon_rect):
					self.Stop=True








