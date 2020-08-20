
import pygame
from pygame import *
import random
import time


#### Most classes will inherit this class; giving them pygame Sprite properties

class Entity(pygame.sprite.Sprite): 
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)

############## COLLIDABLE OBJECTS WHILE IN GAME #####################


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.brick=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Objects/Mario Block.png')
        self.brick=transform.scale(self.brick,(32,32))
        self.image = self.brick 
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)   

    def update(self):
        pass

class Fire(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.fire=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Objects/Fire.png')
        self.fire=transform.scale(self.fire,(32,32))        
        self.image=self.fire
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)   

class Spike(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.spike=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Objects/Spike.png')
        self.spike=transform.scale(self.spike,(32,32))
        self.image=self.spike
        self.image.convert()
        self.rect = Rect(x,y,32,32)

class Star(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.star=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Objects/Star.png')
        self.star=transform.scale(self.star,(64,64))
        self.image=self.star
        self.image.convert()
        self.rect=Rect(x,y,64,64)

#################### ENEMIES ##############################


class Enemy(Entity):
    nbOfEnemies=0    
    def __init__(self, x, y):
        Entity.__init__(self) 
        self.xvel = 0 
        self.yvel = 0 
        self.onGround = False
        self.koopa1=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/rr1.png')
        self.koopa1=transform.scale(self.koopa1,(32,32))
        self.koopa2=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/rr2.png')
        self.koopa2=transform.scale(self.koopa2,(32,32))  
        self.koopa3=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/rr3.png')
        self.koopa3=transform.scale(self.koopa3,(32,32))
        self.goomba=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/GMBA.png')
        self.goomba=transform.scale(self.goomba,(32,32))        
        self.shyguy=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/SHYGUY.png')
        self.shyguy=transform.scale(self.shyguy,(32,32))
        self.EnemyList=[self.koopa1,self.koopa2,self.koopa3,self.goomba,self.shyguy]                    
        self.image=random.choice(self.EnemyList)
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
        Enemy.nbOfEnemies+=1

    def update(self,platforms,mario_characters):
        #Jump Mechanics
        if self.onGround:
             self.yvel -= random.randint(10,25)

        self.xvel = -(random.randint(1,10))
        # While in Air Mechanics:
        self.onGround = False
        if not self.onGround: 
            self.yvel += random.randint(1,10) #Gravity
        # X-Movement:
        self.rect.left += self.xvel
        # X-Axis Collisions:
        self.collide(self.xvel, 0,platforms)
        #self.collide_mario(self.xvel,0,mario_characters)
        # Y-Movement
        self.rect.top += self.yvel
        # Y-Axis Collisions
        self.collide(0, self.yvel,platforms)
        #self.collide_mario(0, self.yvel,mario_characters)

    #Collision with Platform Mechanics    
    def collide(self, xvel, yvel,platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right 
                if yvel > 0:
                    self.rect.bottom = p.rect.top 
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    #Collision with Mario Mechanics
    #def collide_mario(self,xvel, yvel,mario_characters):
        #self.dead=pygame.mixer.Sound('/Users/Zahza/Desktop/smb_mariodie.wav')              
        #for m in mario_characters:
            #if pygame.sprite.collide_rect(self,m):
                #pygame.mixer.music.stop()
                #self.dead.play()
                #time.sleep(3)
                #pygame.event.post(pygame.event.Event(QUIT))

################################################################

class Boss(Entity):
    def __init__(self,x, y):
        Entity.__init__(self) 
        self.xvel = 0 
        self.yvel = 0 
        self.onGround = False 
        self.bowser = image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/Bowser.png')
        self.bowser= transform.scale(self.bowser,(128,128))
        self.image=self.bowser
        self.image.convert()
        self.rect = Rect(x, y, 128, 128) 

    def update(self,platforms,mario_characters):
        #Jump Mechanics
        if self.onGround:
            self.yvel -= 20
        self.xvel = 0     
        # While in Air Mechanics:    
        if not self.onGround: 
            self.yvel += 1 #Gravity
        # X-Movement
        self.rect.left += self.xvel
        # X-Axis Collisions
        self.collide(self.xvel, 0,platforms)
        self.collide_mario(self.xvel,0,mario_characters)
        # Y-Movement
        self.rect.top += self.yvel
        # Y-Axis Collisions
        self.onGround = False
        self.collide(0, self.yvel,platforms)
        self.collide_mario(0, self.yvel,mario_characters)

    def collide(self, xvel, yvel,platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left 
                if xvel < 0:
                    self.rect.left = p.rect.right 
                if yvel > 0:
                    self.rect.bottom = p.rect.top 
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom 

    def collide_mario(self,xvel, yvel,mario_characters):
        self.dead=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/smb_mariodie.wav')              
        for m in mario_characters:
            if pygame.sprite.collide_rect(self,m):
                pygame.mixer.music.stop()
                self.dead.play()
                pygame.event.post(pygame.event.Event(QUIT))



############################ MARIO CHARACTER ########################################


class Player(Entity):
    def __init__(self, x, y): 
        Entity.__init__(self) 
        self.xvel = 0 
        self.yvel = 0 
        self.onGround = False
        self.Mario1=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/Mario Right.png')
        self.Mario1=transform.scale(self.Mario1,(64,64))
        self.Mario2=image.load('/Users/Zahza/Desktop/Mario 3.0/Images/Characters/Mario Left.png')
        self.Mario2=transform.scale(self.Mario2,(64,64))
        self.image=self.Mario1        
        self.image.convert()
        self.rect = Rect(x, y, 64, 64)

    def update(self, up, down, left, right, running, platforms,enemies):
        if up:
            if self.onGround: self.yvel -= 30 
        if down:
            pass
        if running:
            self.xvel = 12 
        if left:
            self.xvel = -10
            self.image=self.Mario2             
        if right:
            self.xvel = 30
            self.image=self.Mario1             
        
        #Mario's Mechanics While in Air:
            
        if not self.onGround: 
            self.yvel += 1.8 #Gravity
        if not(left or right): 
            self.xvel = 0
        # X-Movement
        self.rect.left += self.xvel
        # X-Axis Collisions
        self.collide(self.xvel, 0, platforms)
        self.collide_enemies(self.xvel,0,enemies)
        # Y-Movement
        self.rect.top += self.yvel
        self.onGround = False;
        # Y-Axis Collisions
        self.collide(0, self.yvel, platforms)
        self.collide_enemies(0,self.yvel,enemies)


    def collide(self, xvel, yvel, platforms):
        self.dead=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/smb_mariodie.wav')  
        self.win=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/Super_Mario_Bros_-_Level_Complete.wav')
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, Fire):
                    pygame.mixer.music.stop()
                    self.dead.play()
                    time.sleep(5)
                    pygame.event.post(pygame.event.Event(QUIT))
                    self.Proceed=0                    
                if isinstance(p,Spike):
                    pygame.mixer.music.stop()
                    self.dead.play()
                    time.sleep(5)                    
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p,Star): 
                    pygame.mixer.music.stop()
                    self.win.play()
                    time.sleep(10)
                    self.Proceed=1
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel=-20 
                if xvel < 0:
                    self.rect.left = p.rect.right 
                if yvel > 0:
                    self.rect.bottom = p.rect.top 
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom 
 

    def collide_enemies(self,xvel, yvel,enemies):
        self.dead=pygame.mixer.Sound('/Users/Zahza/Desktop/Mario 3.0/Audio/smb_mariodie.wav')                 
        for e in enemies:
           if pygame.sprite.collide_rect(self,e):
                if xvel > 0:
                    self.rect.right = e.rect.left
                    self.xvel=0
                    pygame.mixer.music.stop()
                    self.dead.play()
                    time.sleep(5)
                    pygame.event.post(pygame.event.Event(QUIT))

                if xvel < 0:
                    self.rect.left = e.rect.right
                    pygame.mixer.music.stop()
                    self.dead.play()
                    time.sleep(5)
                    pygame.event.post(pygame.event.Event(QUIT))                        
                if yvel > 0:
                    self.rect.bottom = e.rect.top 
                    self.onGround = True
                    self.yvel = 0
                    pygame.mixer.music.stop()
                    self.dead.play()
                    time.sleep(5)
                    pygame.event.post(pygame.event.Event(QUIT))                       
                if yvel < 0:
                    self.rect.top = e.rect.bottom


                    
                       
       

