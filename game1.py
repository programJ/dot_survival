import pygame
from pygame import *
import time
import sys
import random

def text_to_screen(screen, background, toprint, size, x=0, y=0):	
	# Display some text
	font = pygame.font.Font('/home/pranjal/Downloads/wps-office_10.1.0.5672~a21_x86_64/fonts/FZKTK.TTF', size)
	text = font.render(toprint, 2, (250, 250, 250))
	textpos = text.get_rect()
	#textpos.centerx = background.get_rect().centerx
	background.blit(text, (x,y))

	# Blit everything to the screen
	return background

def collision(x,y):
	if x>=width-20 or x<=0 or y>=height-20 or y<=0:
		return 1

def game(screen):
	# 3 - Load images
		player = pygame.image.load("/home/pranjal/Pranjal/fun_my_games/green_square.png")
		Vx=0.1
		Vy=0.1
		vx=0
		vy=0
		x=100
		y=100
		score=0
		t=0

		while 1:
			screen.fill((250, 250, 250))
			x=x+(vx)
			y=y+(vy)
			
			if collision(x,y):	#checking if player is inside the boundaries or not
				t=time.time()
				score=int((t-t0)*10)			
				break
			
			screen.blit(player, (x,y))
		    	pygame.display.flip()
		    	
			keys=pygame.key.get_pressed()	#controler key input
			
			if t==0 and (keys[K_LEFT] or keys[K_UP] or keys[K_RIGHT] or keys[K_DOWN]):
				t0=time.time()	#setting up start time
	
			if keys[K_LEFT]:
		    		vx=-Vx
				vy=0
				t=t+1
		    	if keys[K_UP]:
				vx=0
				vy=-Vy
				t=t+1
			if keys[K_RIGHT]:
		    		vx=Vx
				vy=0
				t=t+1
		    	if keys[K_DOWN]:
				vx=0
				vy=Vy
				t=t+1

		    	for event in pygame.event.get():	# check if the event is the X button 
				if event.type==pygame.QUIT:	    # if it is quit the game
			    		pygame.quit() 
			    		exit(0) 

		print "game over"
		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((250, 0, 0))

		background=text_to_screen(screen, background, "Game Over", 50)
		background=text_to_screen(screen, background, "You have scored: "+str(score), 20, 50, 50)
		background=text_to_screen(screen, background, "Play again: (Yes : space 	No : press backspace): ", 20, 10, 350)
		screen.blit(background, (0, 0))
		pygame.display.flip()
		return


if __name__ == '__main__':
	pygame.init()
	width, height = 640, 480
	screen=pygame.display.set_mode((width, height))

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 0, 0))
	background=text_to_screen(screen, background, "The Dot survival", 50)
	background=text_to_screen(screen, background, "Star playing	(press space) ", 30, 10, 250)
	background=text_to_screen(screen, background, "Exit game	(press backspace): ", 20, 10, 300)
	screen.blit(background, (0, 0))
	pygame.display.flip()		

	
	while 1:
		will=pygame.key.get_pressed()
		if will[K_SPACE]:
			game(screen)
		if will[K_BACKSPACE]:
			sys.exit()			
			break

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit(0)
