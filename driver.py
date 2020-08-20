import pygame
from pygame import *
import random
import time
import gamescreen
import startscreen
import instructionscreen
import mariolives
import gameover


def main():

	window1=startscreen.StartScreen()
	window1.Run()
	window2=instructionscreen.InstructionScreen()
	window2.Run()
	window3=mariolives.ThreeLives()
	window3.Run()	
	window4=gamescreen.LevelOne()
	window4.Run()
	window5=mariolives.TwoLives()
	window5.Run()
	window6=gamescreen.LevelOne()
	window6.Run()
	window7=mariolives.OneLives()
	window7.Run()
	window8=gamescreen.LevelOne()
	window8.Run()
	window9=gameover.GameOver()
	window9.Run()

main()


