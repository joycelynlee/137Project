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

global chatSocket
global lobby_id
global name
global chat_log
global chat_client
global chatlogui
chatlogui = []

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
playerImg = pygame.image.load('Images/player.png')
food1Img = pygame.image.load('Images/kopiko.png')
food2Img = pygame.image.load('Images/bluebook.png')
chatbgImg = pygame.image.load('Images/chat_background.png')
scImg = pygame.image.load('Images/score_board.png')
scoreImg = pygame.image.load('Images/score.png') 

# main menu images
htppgImg = pygame.image.load('Images/how_to_play_page.png')
backImg = pygame.image.load('Images/back.png')
playImg = pygame.image.load('Images/play1.png')
htpImg = pygame.image.load('Images/how_to_play.png')
quitImg = pygame.image.load('Images/quit.png')
aplayImg = pygame.image.load('Images/a_play.png')
ahtpImg = pygame.image.load('Images/a_how_to_play.png')
aquitImg = pygame.image.load('Images/a_quit.png')
abackImg = pygame.image.load('Images/a_back.png')

# quit game pop up images
nextlevelImg = pygame.image.load('Images/next_level.png')
xbuttonImg = pygame.image.load('Images/x_button.png')
exitImg = pygame.image.load('Images/exit.png')
cancelImg = pygame.image.load('Images/cancel.png')
axbuttonImg = pygame.image.load('Images/a_x_button.png')
aexitImg = pygame.image.load('Images/a_exit.png')
acancelImg = pygame.image.load('Images/a_cancel.png')
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
		bigText = pygame.font.Font("freesansbold.ttf", 15)
		textSurf, textRect =  text_objects(str(self.score), bigText, gray)
		window.blit(textSurf, (1140, 625\

			))	

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

###################################### game #############################################
def show_score():
	window.blit(scoreImg, (1040, 618))	

def show_sc():
	img = pygame.transform.scale(scImg, (150, 150))
	window.blit(img, (1045, 5))

###################################### chat #############################################
def show_chat():
	window.blit(chatbgImg, (0, 390))

def showChatLog(addmsgs):
	index = 0
	for word in addmsgs:	
		bigText = pygame.font.Font("freesansbold.ttf", 15)
		textSurf, textRect =  text_objects(str(addmsgs[index]), bigText, gray)
		window.blit(textSurf, (20, 410+(18*index)))	
		index += 1

def updateChatLog(templog):
	global chatlogui	
	if(len(templog) <= 10):
		chatlogui = templog
	else:
		del templog[0]
		chatlogui = templog

def sendMessage(msg):
    global name
    packet = tcp_packet_pb2.TcpPacket.ChatPacket()
    packet.type = 3
    packet.message = msg
    packet.player.name = name
    chatSocket.send(packet.SerializeToString())

def chatListenerGUI():
    global chat_log
    while True:
        packet = tcp_packet_pb2.TcpPacket()
        data = chatSocket.recv(1024)
        data1 = data
        packet.ParseFromString(data1)
        if packet.type == 0:
            packet = tcp_packet_pb2.TcpPacket.DisconnectPacket()
            packet.ParseFromString(data)
            if packet.update == 0:
                chat_log = chat_log + '\n' + packet.player.name + " has disconnected!"
            elif packet.update == 1:
                chat_log = chat_log + '\n' + packet.player.name + " has lost connection!"
        elif packet.type == 1:
            packet = tcp_packet_pb2.TcpPacket.ConnectPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + packet.player.name + " successfully connected to lobby " + packet.lobby_id
        elif packet.type == 2:
            packet = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + "Lobby " + packet.lobby_id + " successfully created!"
        elif packet.type == 3:
            packet = tcp_packet_pb2.TcpPacket.ChatPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + packet.player.name + ": " + packet.message
        elif packet.type == 4:
            packet = tcp_packet_pb2.TcpPacket.PlayerListPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + packet.player_list
        elif packet.type == 5:
            packet = tcp_packet_pb2.TcpPacket.ErrLdnePacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + "Error: " + packet.err_msg
        elif packet.type == 6:
            packet = tcp_packet_pb2.TcpPacket.ErrLfullPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + "Error: " + packet.err_msg
        elif packet.type == 7:
            packet = tcp_packet_pb2.TcpPacket.ErrPacket()
            packet.ParseFromString(data)
            chat_log = chat_log + '\n' + "Error: " + packet.err_msg

def chatListener():
	global chatSocket
	templog = []
	while True:
		packet = tcp_packet_pb2.TcpPacket()
		data = chatSocket.recv(1024)
		data1 = data
		packet.ParseFromString(data1)
		if packet.type == 0:
			packet = tcp_packet_pb2.TcpPacket.DisconnectPacket()
			packet.ParseFromString(data)
			if packet.update == 0:
				print(packet.player.name, " has disconnected!")
				templog.append(packet.player.name + " has disconnected!")
			elif packet.update == 1:
				print(packet.player.name, " has lost connection!")
				templog.append(packet.player.name + " has lost connection!")
		elif packet.type == 1:
			packet = tcp_packet_pb2.TcpPacket.ConnectPacket()
			packet.ParseFromString(data)
			print(packet.player.name, " successfully connected to lobby ", packet.lobby_id)
			templog.append(packet.player.name + " successfully connected to lobby " + packet.lobby_id)
		elif packet.type == 2:
			packet = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
			packet.ParseFromString(data)
			print("Lobby ", packet.lobby_id, " successfully created!")
			templog.append("Lobby " + packet.lobby_id + " successfully created!")
		elif packet.type == 3:
			packet = tcp_packet_pb2.TcpPacket.ChatPacket()
			packet.ParseFromString(data)
			print(packet.player.name, ": ", packet.message)
			templog.append(packet.player.name + ": " + packet.message)
		elif packet.type == 4:
			packet = tcp_packet_pb2.TcpPacket.PlayerListPacket()
			packet.ParseFromString(data)
			print(packet.player_list)
			templog.append(packet.player_list)
		elif packet.type == 5:
			packet = tcp_packet_pb2.TcpPacket.ErrLdnePacket()
			packet.ParseFromString(data)
			print("Error: ", packet.err_message)
			templog.append("Error: " + packet.err_message)
		elif packet.type == 6:
			packet = tcp_packet_pb2.TcpPacket.ErrLfullPacket()
			packet.ParseFromString(data)
			print("Error: ", packet.err_message)
			templog.append("Error: " + packet.err_message)		
		elif packet.type == 7:
			packet = tcp_packet_pb2.TcpPacket.ErrPacket()
			packet.ParseFromString(data)
			print("Error: ", packet.err_message)
			templog.append("Error: " + packet.err_message)		
		updateChatLog(templog)

def createLobby(max_players):
	global socket
	packet = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
	packet.type = 2
	packet.max_players =  max_players
	socket.send(packet.SerializeToString())
	data = socket.recv(1024)
	packet.ParseFromString(data)
	return packet.lobby_id

def startChat(name, lobby_id):
	global chatSocket

	chatSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	chatSocket.connect(('202.92.144.45', 80))

	chatListenerThread = threading.Thread(target = chatListener)
	chatListenerThread.daemon = True
	chatListenerThread.start()

	packet = tcp_packet_pb2.TcpPacket.ConnectPacket()
	packet.type = 1
	packet.lobby_id = lobby_id
	packet.player.name = name
	chatSocket.send(packet.SerializeToString())

def startGame():
	global name
	global lobby_id
	##########################
	#	SOURCE:
	#	https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
	##########################

	font = pygame.font.Font(None, 32)
	clock = pygame.time.Clock()
	input_box = pygame.Rect(530, 309, 140, 32)
	color_inactive = pygame.Color('lightskyblue3')
	color_active = pygame.Color('dodgerblue2')
	color = color_inactive
	active = False
	text = 'Enter name here'
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				# If the user clicked on the input_box rect.
				if input_box.collidepoint(event.pos):
					# Toggle the active variable.
					active = not active
					text = ''
				else:
					active = False
				# Change the current color of the input box.
				color = color_active if active else color_inactive
			if event.type == pygame.KEYDOWN:
				if active:
					if event.key == pygame.K_RETURN:
						name = text
						done = True
						text = 'Enter lobby id here'
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

		window.fill((30, 30, 30))
		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Resize the box if the text is too long.
		width = max(200, txt_surface.get_width()+10)
		input_box.w = width
		# Blit the text.
		window.blit(txt_surface, (input_box.x+5, input_box.y+5))
		# Blit the input_box rect.
		pygame.draw.rect(window, color, input_box, 2)

		pygame.display.flip()
		clock.tick(30)

	active = False
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				# If the user clicked on the input_box rect.
				if input_box.collidepoint(event.pos):
					# Toggle the active variable.
					active = not active
					text = ''
				else:
					active = False
				# Change the current color of the input box.
				color = color_active if active else color_inactive
			if event.type == pygame.KEYDOWN:
				if active:
					if event.key == pygame.K_RETURN:
						lobby_id = text
						done = True
						text = ''
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

		window.fill((30, 30, 30))
		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Resize the box if the text is too long.
		width = max(200, txt_surface.get_width()+10)
		input_box.w = width
		# Blit the text.
		window.blit(txt_surface, (input_box.x+5, input_box.y+5))
		# Blit the input_box rect.
		pygame.draw.rect(window, color, input_box, 2)

		pygame.display.flip()
		clock.tick(30)

	startChat(name, lobby_id)
#########################################################################################
def game_loop():
	x = (SCREEN_WIDTH * 0.45)
	y = (SCREEN_HEIGHT * 0.45)
	player = Player(x, y)
	
	font = pygame.font.Font(None, 25)
	clock = pygame.time.Clock()
	input_box = pygame.Rect(10, 600, 140, 25)
	color_inactive = pygame.Color(('gray'))
	color_active = pygame.Color('black')
	color = color_inactive
	active = False
	text = 'Enter message here'
	done = False

	while not done:
		window.fill(background)
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				exit_game(1)
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				# If the user clicked on the input_box rect.
				if input_box.collidepoint(event.pos):
					# Toggle the active variable.
					active = not active
					text = ''
				else:
					active = False
				# Change the current color of the input box.
				color = color_active if active else color_inactive
			if event.type == pygame.KEYDOWN:
				if active:
					if event.key == pygame.K_RETURN:
						# chat_client.sendMessage(text)
						sendMessage(text)
						active = False
						color = color_active if active else color_inactive
						text = 'Enter message here'
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode	
				else:
					if event.key == pygame.K_RETURN:
						active = not active
						text = ''
						color = color_active if active else color_inactive

		player.update()
	
		spawn_food(len(FOOD))
		for item in FOOD:
			item.render(window)

		player.render(window)

		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Resize the box if the text is too long.
		width = max(200, txt_surface.get_width()+10)
		input_box.w = width
		# Blit the text.
		window.blit(txt_surface, (input_box.x+5, input_box.y+5))
		# Blit the input_box rect.
		pygame.draw.rect(window, color, input_box, 2)

		show_chat()
		show_sc()
		show_score()
		showChatLog(chatlogui)

		# show_chat(socket)
		pygame.display.update()

		clock.tick(50)

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def actions(action):
	if action == 1:
		startGame()
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
	global  chat_log
	chat_log = ''
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
