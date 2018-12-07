####### imports for game #######
import pygame
import random
import math
################################

####### imports for chat #######
import player_pb2
import tcp_packet_pb2
import socket
import os
import threading
################################

from ctypes import *
from tkinter import *

pygame.init()
pygame.font.init()


background = (255, 255, 255)
black = (0, 0, 0)
a_black = (169, 169, 169)
gray = (105, 105, 105)
white = (255, 255, 255)
red = (255, 0, 0)
a_red = (255, 150, 150)
green = (0, 255, 0)
a_green = (150, 255, 150)
blue = (0, 0, 255)
a_blue = (150, 150, 255)
maroon = (110, 10, 1)

SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AGARIO")
pygame.display.update()

clock = pygame.time.Clock()

FOOD = []
############################################
# game images
playerImg = pygame.image.load('player.png')
food1Img = pygame.image.load('kopiko.png')
food2Img = pygame.image.load('bluebook.png')
chatbgImg = pygame.image.load('chat_background.png')

# main menu images
htppgImg = pygame.image.load('how_to_play_page.png')
backImg = pygame.image.load('back.png')
playImg = pygame.image.load('play1.png')
htpImg = pygame.image.load('how_to_play.png')
quitImg = pygame.image.load('quit.png')
aplayImg = pygame.image.load('a_play.png')
ahtpImg = pygame.image.load('a_how_to_play.png')
aquitImg = pygame.image.load('a_quit.png')
abackImg = pygame.image.load('a_back.png')


# quit game pop up images
nextlevelImg = pygame.image.load('next_level.png')
xbuttonImg = pygame.image.load('x_button.png')
exitImg = pygame.image.load('exit.png')
cancelImg = pygame.image.load('cancel.png')
axbuttonImg = pygame.image.load('a_x_button.png')
aexitImg = pygame.image.load('a_exit.png')
acancelImg = pygame.image.load('a_cancel.png')
############################################

def getDistance(pos1,pos2):
    px,py = pos1
    p2x,p2y = pos2
    diffX = math.fabs(px-p2x)
    diffY = math.fabs(py-p2y)

    return ((diffX**2)+(diffY**2))**(0.5)

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y 
		self.speed = 1
		self.level = 1
		self.score = 0
		self.size = 100
		self.location = (x,y)
		self.destination = self.location
		self.stopDis = 5
		self.img = pygame.transform.scale(playerImg, (40, 40))

	def update(self):
		self.move()
		self.collisionDetection()
		self.level_up()

	def level_up(self):
		if self.score/(self.level*10) > 1:
			self.level += 1
			self.size = self.size*1.2
			self.img = pygame.transform.scale(playerImg, (int(self.size), int(self.size)))
	def move(self):
		cX, cY = pygame.mouse.get_pos()
		self.destination = (cX, cY)
		selfPosX, selfPosY = self.location

		disToDes = (cX-selfPosX, cY-selfPosY)
		if disToDes[0] > 0:
			disToDes = (disToDes[0]+self.stopDis, disToDes[1])  #If the distance is less than 0, add the stopping distance
		if disToDes[1] > 0:
			disToDes = (disToDes[0], disToDes[1]+self.stopDis)
		
		disToAdd = (int(disToDes[0]),int(disToDes[1]))    #Add distance/speed to current location to get a new location
		self.location = (self.location[0]+disToAdd[0], self.location[1]+disToAdd[1])
		self.x = self.location[0]
		self.y = self.location[1]
		cursor_rect = (self.img).get_rect()
		cursor_rect.center = (self.x, self.y)
		self.x = cursor_rect[0]
		self.y = cursor_rect[1]

	def collisionDetection(self):
		for item in FOOD:
			if(getDistance((item.x, item.y), (self.x, self.y)) <= ((self.size/1.8)+45)):
				self.score += 1
				FOOD.remove(item)

	def render(self, window):
		if(self.score == 0):
			self.img = pygame.transform.scale(playerImg, (100, 100))
		window.blit(self.img, (self.x, self.y))

class Food(object):
	def __init__(self):
		self.x = random.randint(10, SCREEN_WIDTH-10)
		self.y = random.randint(10, SCREEN_HEIGHT-10)
		self.pic = random.randint(1, 2)
		self.size = 90
		self.location = (self.x, self.y)

	def render(self, window):
		if self.pic == 1:
			displayImg = pygame.transform.scale(food1Img, (self.size, self.size))			
		if self.pic == 2:
			displayImg = pygame.transform.scale(food2Img, (self.size, self.size))			
		window.blit(displayImg, (self.x, self.y))

def spawn_food(amountOfFood):
	if(amountOfFood < 5):
		food = Food()
		FOOD.append(food)
		amountOfFood = amountOfFood + 1

###################################### chat #############################################
def show_chat(socket):
	mouse = pygame.mouse.get_pos()
	window.blit(chatbgImg, (0, 390))

#########################################################################################
def game_loop():
	x = (SCREEN_WIDTH * 0.45)
	y = (SCREEN_HEIGHT * 0.45)
	player = Player(x, y)
	
	while(True):
		window.fill(background)

		for e in pygame.event.get():
			if(e.type == pygame.QUIT):
				exit_game(1)
		player.update()
		player.render(window)
		
		spawn_food(len(FOOD))
		for item in FOOD:
			item.render(window)

		show_chat(socket)
		pygame.display.update()

		clock.tick(50)

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def actions(action):
	if action == 1:
		game_loop()
	if action == 2:
		main()
	if action == 3:
		go_to_how_to_play()
	if action == 4:
		exit_game(1)

	if action == 5:
		pygame.quit()
		quit()

def menu_button(mouse, x, y, w, h, i_x, i_y, i_img, a_img, action):
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		window.blit(a_img, (i_x, i_y))
		if click[0] == 1:
			actions(action)				
	else:
		window.blit(i_img, (i_x, i_y))

def show_how_to_play():
	mouse = pygame.mouse.get_pos()
	window.blit(htppgImg, (0, 0))
	menu_button(mouse, 1080, 570, 110, 50, 1030, 570, backImg, abackImg, 2)	

def go_to_how_to_play():
	while(True):
		window.fill(background)

		for e in pygame.event.get():
			if(e.type == pygame.QUIT):
				exit_game(3)

		show_how_to_play()

		pygame.display.update()
		clock.tick(20)	

def exit_game(page):
	while(True):
		window.fill(background)

		for e in pygame.event.get():
			if(e.type == pygame.QUIT):
				exit_game()

		mouse = pygame.mouse.get_pos()
		window.blit(nextlevelImg, (SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2-75))
		menu_button(mouse, SCREEN_WIDTH/2+52, SCREEN_HEIGHT/2-72, 20, 20, SCREEN_WIDTH/2+52, SCREEN_HEIGHT/2-72, xbuttonImg, axbuttonImg, page)
		menu_button(mouse, SCREEN_WIDTH/2-58, SCREEN_HEIGHT/2-20, 100, 20, SCREEN_WIDTH/2-98, SCREEN_HEIGHT/2-20, exitImg, aexitImg, 5)
		menu_button(mouse, SCREEN_WIDTH/2-58, SCREEN_HEIGHT/2+10, 100, 20, SCREEN_WIDTH/2-98, SCREEN_HEIGHT/2+10, cancelImg, acancelImg, page)				
		pygame.display.update()
		clock.tick(20)

def create_menu():
	bigText = pygame.font.Font("freesansbold.ttf", 80)
	textSurf, textRect =  text_objects("AGAR.IO", bigText, maroon)
	textRect.center = (((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)-20))
	window.blit(textSurf, textRect)

	mouse = pygame.mouse.get_pos()
	menu_button(mouse, 550, 350, 100, 50, 500, 350, playImg, aplayImg, 1)
	menu_button(mouse, 550, 410, 100, 50, 500, 410, htpImg, ahtpImg, 3)
	menu_button(mouse, 550, 470, 100, 50, 500, 470, quitImg, aquitImg, 4)	

def main():
	while(True):
		window.fill(background)

		for e in pygame.event.get():
			if(e.type == pygame.QUIT):
				exit_game(2)

		create_menu()

		pygame.display.update()
		clock.tick(80)	

main()
pygame.quit()
quit()