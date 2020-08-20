import pygame
from pygame import *
import random
import time
import level
import characters


############## CAMERAS ###############################################

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
	WIN_WIDTH=80
	WIN_HEIGHT=600
	HALF_WIDTH=int(WIN_WIDTH / 2)
	HALF_HEIGHT=int(WIN_HEIGHT / 2)	
	l, t, _, _ = target_rect
	_, _, w, h = camera
	return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
	WIN_WIDTH=800
	WIN_HEIGHT=600
	HALF_WIDTH=int(WIN_WIDTH / 2)
	HALF_HEIGHT=int(WIN_HEIGHT / 2)
	l, t, _, _ = target_rect
	_, _, w, h = camera
	l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h
	l = min(0, l)                           # stop scrolling at the left edge
	l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
	t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
	t = min(0, t)                           # stop scrolling at the top
	return Rect(l, t, w, h)

##########################################################################	

class LevelOne():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.display.set_caption("Level 1-1")
		pygame.mixer.music.load('/Users/Zahza/Desktop/Mario 3.0/Audio/StayAlert_.wav')
		pygame.mixer.music.play(-1)
		x=0
		y=0
		self.WIN_WIDTH=800
		self.WIN_HEIGHT=600
		self.DISPLAY=(self.WIN_WIDTH,self.WIN_HEIGHT)
		self.DEPTH=32
		self.FLAGS=0
		self.CAMERA_SLACK=30
		global cameraX, cameraY
		self.screen = pygame.display.set_mode(self.DISPLAY, self.FLAGS, self.DEPTH)
		self.background=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Mario Background.png')
		self.background=transform.scale(self.background,(self.WIN_WIDTH,self.WIN_HEIGHT))
		self.background.convert()
		self.timer = pygame.time.Clock()
		self.jump=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/smb_jump-small.wav')
		self.dead=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/smb_mariodie.wav')
		self.entities=pygame.sprite.Group()

#################### VARIABLES #######################

		self.max_enemies=3
		self.up=False
		self.down=False
		self.left=False
		self.right=False
		self.running=False
		self.platforms=[]
		self.spikes=[]
		self.enemies = []
		self.stars= []
		self.fire= []
		self.start_ticks=pygame.time.get_ticks()
		self.mario=characters.Player(1200,2100)
		self.mario_characters=[self.mario]
		self.entities.add(self.mario)
		self.minion1=characters.Enemy(1900,2100)
		self.minion2=characters.Enemy(1700,2100)
		self.minion3=characters.Enemy(1800,2100)								
		self.bowser=characters.Boss(400,1400)
		self.enemies =[self.bowser,self.minion1,self.minion2,self.minion3]
		for e in self.enemies:
			self.entities.add(e)		

########## GAME LEVEL #################

		self.level=[





			"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",																																																																																																																																																																																																																								
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																															 	P",
			"P																																																																																																																																																																																																																P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																																																																																															    P",
			"P																																																																																																																																													P																																																																			P",
			"P																																																																																																																																													P																																																																			P",
			"P																																																																																																																																													P																																																																			P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                                                                                                                                                      T                    P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                                                                                                                                                                           P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                                                                                                                                               PPPPPPPPPPPPP               P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                                                                                                                                            PPPPPPPPPPPPPPPPPPP            P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                                                                                                      PPPPPPPP                           PPPPPPPPPPPPPPPPPPPPPPPPP         P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                                               SSSSSSSSSSSS                         SSSSSSSS                        PPPPPPPPPPPP                      PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                              PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                                                                                     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                  PPPPPPPPPPP                 PPPPPPPPPPPP                     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                                  PPPPPPPPPPP                 PPPPPPPPPPPPP                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", 
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   SSSS       PPPPPPPPPPPPPPP                 PPPPPPPPPPPPPPPP            PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   PPPPPPPPPPPPPPPPPPPPPPPPPPEEEEEEEEEEEEEEEEEPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P         PPPPPPPP  P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",   
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",        
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",  
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P  SSS              P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P  PPPPPPPP         P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",                                                                                     
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  P                   P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         P                   P",           
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         P                   P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         P        PPPPPPPP   P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         P                   P", 
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                                             P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                                             P", 
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         SSS            		P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                         PPPPPPPP            P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                        P                                                                                                                                                                             P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                 SSS    P                                                                                                                                                                             P", 
			"P                                                                                                                                                                                                                                                                                        PPPPPPPPPPP                                                                                         PPPPPPPPP         PPPPPPPPPP                                                                                                                                                                             	P",
			"P                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           SSS        P",
			"P                                                                                                                                                                                                                                                                              SSSSS                      SSSSS                                                                                                                                                                                                                                                                          PPPPPPP       P",                                  
			"P                                                                                                                                                                                                                                                                     PPPPPPPPPPPPPP                      PPPPPPPPPPPPP                                                                                                                                                                                                                                                                                P",                
			"P                                                                                                                     PPPPPPPPP                                                                                                                                                   PP                      PP                                                                          PPPPPPPP               PPPPPPPPPPPPPPP                                                                                                                                                                           P",          
			"P                                                                                                                                                                                       PPPPPPPPP           PPPPPPPPP                                                             PP                      PP                                                                                                                                                                                                                                                                           PPPPPPP         P",                                
			"P                                                                                                                               SSS                                                   PPPPP                       PPPPP                                            SSSSSSS        PP                      PP                                                                             SSSSS                                                                                                                                                                                       PPPPPPPPPPP       P",                                      
			"P                                                                                                            PPPPPPPPP          PPPPPPPPPPP                                     PPPPPPPPPPP                       PPPPPPPPPPP                                 PPPPPPPPPPPP        PP                      PP                                                                            PPPPPPPPPPP                SSSSSS                   PPPPPPPPSSS                                                                              PPPPPPPPPPPP                             PPPPPPPPPPPPPPPPPPPPPPPPPP",                                                             
			"P                         SS       SS                               SSSS                           SS    	PPPPP                        PPPPP                                                                              PP                                                     PP                      PP                           PPPPPPPP                                                                   PPPPPPPPPPPPPPP           PPPPPPPPPPPPSSS                                                                          PPPPPPPPPPPPPPPP                         P",                                                   
			"P                         PPPPPPPPPPP            PP                PPPPPP                        SSPPPPPPPPPPPP                         PPPPPPPPPPPP                                                                       PP                                                     PP                      PP                           PPPPPPPP                             PPPPPPPP                                                        PPPPPPPPPPPPPPPPSSSS                                                        SSS          PPPPPPPPPPPPPPPPPPPP                     P",                                                  
			"P                                                PP              PPPPPPPPPP                    SPPPPP                                           PPPPP                 PPP                                                  PP                         PPPP                                                PP                           PPPPPPPP                          PPPPPPPPPPP                                                        PPPPPPPPPPPPPPPPPPPPPPPP                                 PPPP          PPPPPPPP          PPPPPPPPPPPPPPPPPPPPPPPP                 P",                                                     
			"P                                                PP             PPPPPPPPPPPP                 SPPPPPPP                                           PPPPPPP               PPP                                                  PP                      PPPPPPP                                                PP                           PPPPPPPP                       PPPPPPPPPPPPPP                                                        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                         PPPP          PPPPPPPP          PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP           P",                                                          
			"P                                                PP    SSS    PPPPPPPPPPPPPPPP            SSPPPPPPPPP               SSSSSSSSSSSSSS              PPPPPPPPP    SSSSS    PPP                                 SSSSSSSSSSSSS    PP  SSS             PPPPPPPPPPP                                                PP           SSSSSSSS        PPPPPPPP                  PPPPPPPPPPPPPPPPPPP                                                        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP            PPPP          PPPPPPPP          PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     P",                                                        
			"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEEEEEEEEEEEEPPPPPPPPPPPPPPPPPPPPPPPPPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEEEEEEEEEEEEPPPPEEEEEEEEEEPPPPPPPPEEEEEEEEEEPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
		
##### Creates the objects for the level ##########

		for row in self.level:
			for column in row:
				if column == "P":
					p = characters.Platform(x,y)
					self.platforms.append(p)
					self.entities.add(p)
				if column == "E":
					e = characters.Fire(x,y)
					self.platforms.append(e)
					self.entities.add(e)
				if column == "S": 
					s = characters.Spike(x,y)
					self.platforms.append(s)
					self.entities.add(s)
				if column == "T":
					t = characters.Star(x,y)
					self.platforms.append(t)
					self.entities.add(t)	
				x += 32 
			y += 32
			x = 0

######### Required for the camera movement ###########

		self.total_level_width=len(self.level[0])*32
		self.total_level_height=len(self.level)*32

############# CREATION AND DESTRUCTION OF ENEMY OBJECTS ####################
  	
	def RemoveWave1(self):
		self.entities.remove(self.minion1)
		self.entities.remove(self.minion2)
		self.entities.remove(self.minion3)				
		del self.enemies[1:4]

	def CreateWave2(self):
		self.minion1=characters.Enemy(1300,2300)
		self.minion2=characters.Enemy(700,2300)
		self.minion3=characters.Enemy(1800,2300)
		A=[self.minion1,self.minion2,self.minion3]
		for i in A:
			self.entities.add(i)
			self.enemies.append(i)

	def RemoveWave2(self):
		self.entities.remove(self.minion1)
		self.entities.remove(self.minion2)
		self.entities.remove(self.minion3)				
		del self.enemies[1:4]			

	def CreateWave3(self):
		self.minion1=characters.Enemy(3600,2100)
		self.minion2=characters.Enemy(3800,2100)
		self.minion3=characters.Enemy(3900,2100)
		A=[self.minion1,self.minion2,self.minion3]
		for i in A:
			self.entities.add(i)
			self.enemies.append(i)

	def RemoveWave2(self):
		self.entities.remove(self.minion1)
		self.entities.remove(self.minion2)
		self.entities.remove(self.minion3)				
		del self.enemies[1:4]			

	def CreateWave3(self):
		self.minion1=characters.Enemy(8700,2100)
		self.minion2=characters.Enemy(8900,2100)
		self.minion3=characters.Enemy(9100,2100)
		A=[self.minion1,self.minion2,self.minion3]
		for i in A:
			self.entities.add(i)
			self.enemies.append(i)

	def RemoveWave3(self):
		self.entities.remove(self.minion1)
		self.entities.remove(self.minion2)
		self.entities.remove(self.minion3)				
		del self.enemies[1:4]			

	def CreateWave4(self):
		self.minion1=characters.Enemy(17800,2100)
		self.minion2=characters.Enemy(17500,2000)
		self.minion3=characters.Enemy(17300,2200)
		A=[self.minion1,self.minion2,self.minion3]
		for i in A:
			self.entities.add(i)
			self.enemies.append(i)

	def RemoveWave4(self):
		self.entities.remove(self.minion1)
		self.entities.remove(self.minion2)
		self.entities.remove(self.minion3)				
		del self.enemies[1:4]			

	def CreateBoss(self):
		self.bowser=characters.Boss(24000,900)
		A=[self.bowser]
		for i in A:
			self.entities.add(i)
			self.enemies.append(i)									


########## MAIN GAME LOOP #####################

	def Run(self):
		camera=Camera(complex_camera, self.total_level_width, self.total_level_height)		

		self.Stop=False
		while self.Stop==False:			
			self.Event()
			self.timer.tick(120)
			self.seconds=((pygame.time.get_ticks()-self.start_ticks)/1000)-35.0
			self.countdown=360-(((pygame.time.get_ticks()-self.start_ticks)/1000)-35.0)			

			if self.seconds >360: 
				pygame.mixer.music.stop()
				self.dead.play()
				time.sleep(3)
				self.Stop=True
			if round(self.seconds,0)==80:	
				self.RemoveWave1()
				self.CreateWave2()
			if round(self.seconds,0)==120:
				self.RemoveWave2()
				self.CreateWave3()	
			if round(self.seconds,0)==150:
				self.RemoveWave3()
				self.CreateWave4()
			if round(self.seconds,0)==180:
				self.RemoveWave4()
				self.CreateWave5()
			if round(self.seconds,0)==210:
				self.RemoveWave5()
				self.CreateBoss()
					

																												
			self.screen.blit(self.background,(0,0))
			camera.update(self.mario)
			self.mario.update(self.up, self.down, self.left, self.right, self.running, self.platforms,self.enemies)	
			for i in self.enemies:
				i.update(self.platforms,self.mario_characters)	
			for e in self.entities:
				self.screen.blit(e.image, camera.apply(e))

			pygame.display.update()
			print(round(self.countdown,0))
		pygame.quit()

###### EVENT MANAGER #########            

	def Event(self):			
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				self.Stop=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					self.Stop=True
			if event.type == KEYDOWN:
				if event.key == K_UP:
					self.up = True
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					self.down = True
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					self.left = True
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					self.right = True
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					self.running = True
			if event.type == KEYUP:
				if event.key == K_UP:
					self.up = False
					self.jump.play()
			if event.type == KEYUP:
				if event.key == K_DOWN:
					self.down = False
			if event.type == KEYUP:
				if event.key == K_RIGHT:
					self.right = False
			if event.type == KEYUP:
				if event.key == K_LEFT:
					self.left = False




        	

		




















    







    




















        