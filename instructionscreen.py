import pygame
from pygame import *

class InstructionScreen():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.display.set_caption("Instructions")
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Black Background.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.up_arrow=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Up Arrow.png')
		self.up_arrow=transform.scale(self.up_arrow,(100,100))
		self.down_arrow=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Down Arrow.png')
		self.down_arrow=transform.scale(self.down_arrow,(100,100))
		self.right_arrow=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Right Arrow.png')
		self.right_arrow=transform.scale(self.right_arrow,(100,100))
		self.left_arrow=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Left Arrow.png')
		self.left_arrow=transform.scale(self.left_arrow,(100,100))
		self.up_word=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Up.jpg')
		#self.up_word=transform.scale(self.up_word,(50,50))
		self.down_word=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Down.jpg')
		#self.down_word=transform.scale(self.down_word,(50,50))
		self.right_word=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Right.jpg')
		#self.right_word=transform.scale(self.right_word,(50,50))
		self.left_word=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Left.jpg')
		#self.left_word=transform.scale(self.left_word,(50,50))
		self.continue_icon=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Icons/Continue.png')		
		self.continue_rect=pygame.Rect((170,450),(460,85))

	

	def Run(self):
		self.Stop=False
		while self.Stop==False:
			#Add song
			self.Event()
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.continue_icon,(250,450))
			self.screen.blit(self.up_arrow,(350,150))
			self.screen.blit(self.down_arrow,(350,250))
			self.screen.blit(self.right_arrow,(450,250))			
			self.screen.blit(self.left_arrow,(250,250))
			self.screen.blit(self.up_word,(370,130))
			self.screen.blit(self.down_word,(360,360))
			self.screen.blit(self.left_word,(170,290))			
			self.screen.blit(self.right_word,(560,290))
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
				if self.mouserect.colliderect(self.continue_rect):
					self.Stop=True	

				