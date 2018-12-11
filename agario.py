####### imports for game #######
import pygame
import random
import math
import game_packet_pb2
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
pygame.mixer.pre_init(44100, 16, 2, 4096)

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

n = 3
m = 6 # [name, id, xpos, ypos, img, size]
ADVERSARIES = [[-1] * m] * n
global SCOREBOARD
SCOREBOARD = [[-1] * 2] * n

# SOUND #
############################################
global soundFlag
soundFlag = 0

eatSound = pygame.mixer.Sound('Sounds/eat.wav')
goSound = pygame.mixer.Sound('Sounds/game_over.wav')
pygame.mixer.music.load('Sounds/bgm.mp3')

############################################

# IMAGES #
############################################
# game images
global playerImg
global playerImgInt
playerImg = pygame.image.load('Images/player.png')
player1Img = pygame.image.load('Images/player.png')
player2Img = pygame.image.load('Images/player2.png')
player3Img = pygame.image.load('Images/player3.png')

food1Img = pygame.image.load('Images/kopiko.png')
food2Img = pygame.image.load('Images/bluebook.png')
chatbgImg = pygame.image.load('Images/chat_background.png')
scImg = pygame.image.load('Images/score_board.png')
scoreImg = pygame.image.load('Images/score.png') 

# main menu images
htpImg = pygame.image.load('Images/how_to_play.png')
backImg = pygame.image.load('Images/back.png')
playImg = pygame.image.load('Images/play1.png')
quitImg = pygame.image.load('Images/quit.png')
aplayImg = pygame.image.load('Images/a_play.png')
ahtpImg = pygame.image.load('Images/a_how_to_play.png')
aquitImg = pygame.image.load('Images/a_quit.png')
abackImg = pygame.image.load('Images/a_back.png')
nameImg = pygame.image.load('Images/name.png')
lobbyImg = pygame.image.load('Images/lobby.png')

# how to play
global htppage
htppage = 1
htppgImg = pygame.image.load('Images/how_to_play_page.png')
htppg2Img = pygame.image.load('Images/how_to_play_page_2.png')
nextImg = pygame.image.load('Images/next.png')
anextImg = pygame.image.load('Images/a_next.png')
prevImg = pygame.image.load('Images/prev.png')
aprevImg = pygame.image.load('Images/a_prev.png')

# quit game pop up images
nextlevelImg = pygame.image.load('Images/next_level.png')
xbuttonImg = pygame.image.load('Images/x_button.png')
exitImg = pygame.image.load('Images/exit.png')
cancelImg = pygame.image.load('Images/cancel.png')
axbuttonImg = pygame.image.load('Images/a_x_button.png')
aexitImg = pygame.image.load('Images/a_exit.png')
acancelImg = pygame.image.load('Images/a_cancel.png')

startImg = pygame.image.load('Images/start.png')
startBImg = pygame.image.load('Images/start_b.png')
############################################
def drawAdversaries():
	# [name, xpos, ypos, img, score]	
	for i in range(3):
		if ADVERSARIES[i][0] != -1:
			switch(ADVERSARIES[i][3])
			if ADVERSARIES[i][3] == 1:	
				img = player1Img
			elif ADVERSARIES[i][3] == 2:					
				img = player2Img	
			elif ADVERSARIES[i][3] == 3:					
				img = player3Img

			if(ADVERSARIES[i][4] == 0):
				img2 = pygame.transform.scale(img, (100, 100))
			else:
				size = score/10
				temp = 90
				for i in size:
					size = temp * 1.2
					temp = size
			window.blit(img2, (temp,temp))

def updateScoreBoard(player, name):
	global SCOREBOARD
	SCOREBOARD.clear()
	SCOREBOARD.append(['jm', 20])
	SCOREBOARD.append(['kate', 10])
	for i in range(3):
		if ADVERSARIES[i][0] != -1:
			SCOREBOARD.append([ADVERSARIES[i][0], ADVERSARIES[i][5]])
	index = 0
	SCOREBOARD.append([name, player.get_score()])
	SCOREBOARD.sort(key=lambda x: x[1], reverse=True)
	for word in SCOREBOARD:	
		bigText = pygame.font.Font("freesansbold.ttf", 15)
		textSurf, textRect =  text_objects(str(SCOREBOARD[index]), bigText, maroon)
		window.blit(textSurf, (1072, 40+(33*index)))	
		index += 1

def getDistance(pos1,pos2):
    px,py = pos1
    p2x,p2y = pos2
    diffX = math.fabs(px-p2x)
    diffY = math.fabs(py-p2y)

    return ((diffX**2)+(diffY**2))**(0.5)

class Player(threading.Thread):
	def __init__(self, name, x, y):
		threading.Thread.__init__(self)
		self.name = name
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

	def get_name(self):
		return self.name

	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y

	def get_score(self):
		return self.score

	def get_level(self):
		return self.score/10+1

	def get_size(self):
		return self.get_level()*10

	def get_speed(self): #amount of time in ms it takes for player to move 100u
		return self.get_size()/5

	def get_img(self):
		return self.img

	def get_image(self):
		return 1

	def get_score(self):
		return self.score

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
		# destination(cX, cY)
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
			if(getDistance((item.x+(item.size/2), item.y+(item.size/2)), (self.x+(self.size/2), self.y+(self.size/2))) <= self.size):
				pygame.mixer.Sound.play(eatSound)
				self.score += 1
				FOOD.remove(item)

		# [name, id, xpos, ypos, img, score]	
		for i in range(3):
			if ADVERSARIES[i][0] != -1:
				advx = ADVERSARIES[i][1]
				advy = ADVERSARIES[i][2]
				advimg = ADVERSARIES[i][3]
				advsize = ADVERSARIES[i][4]
				if(getDistance((advx+(advsize/2), advy+(advsize/2)), (self.x+(self.size/2), self.y+(self.size/2))) <= self.size):
					if(self.size > advsize):
						pygame.mixer.Sound.play(eatSound)
						self.score += 1
						ADVERSARIES.remove(i)
					else:
						pygame.mixer.Sound.play(goSound)
						#end game call for the continue box

	def render(self, window):
		if(self.score == 0):
			self.img = pygame.transform.scale(playerImg, (100, 100))
		window.blit(self.img, (self.x, self.y))
		bigText = pygame.font.Font("freesansbold.ttf", 15)
		textSurf, textRect =  text_objects(str(self.score), bigText, gray)
		window.blit(textSurf, (1140, 625))	

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
###################################### choose player ######################
def choose_player_img():
	global playerImg
	bigText = pygame.font.Font("freesansbold.ttf", 40)
	textSurf, textRect =  text_objects("Select Player", bigText, maroon)	
	while(True):
		window.fill(background)

		for e in pygame.event.get():
			if(e.type == pygame.QUIT):
				exit_game(1)

		window.blit(textSurf, (475, 380))
		mouse = pygame.mouse.get_pos()
		a = pygame.transform.scale(playerImg, (200, 200))
		b = pygame.transform.scale(player2Img, (200, 200))
		c = pygame.transform.scale(player3Img, (200, 200))
		menu_button(mouse, 220, 140, 200, 200, 220, 140, a, a, 11)
		menu_button(mouse, 500, 140, 200, 200, 500, 140, b, b, 12)
		menu_button(mouse, 780, 140, 200, 200, 780, 140, c, c, 13)				
		
		pygame.display.update()
		clock.tick(20)	

###################################### game #############################################
def show_score():
	window.blit(scoreImg, (1040, 618))	

def show_sc():
	img = pygame.transform.scale(scImg, (150, 150))
	window.blit(img, (1045, 5))

def gamePacketListener():
	# global game_socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('192.168.0.74', 1219))
	# game_socket.bind(('192.168.0.74', 1218))
	while True:
		data = sock.recv(1024)
		packet = game_packet_pb2.GamePacket.MovePacket()
		packet.ParseFromString(data)
		print(packet.player.name, "has moved to (", packet.newX, ",", packet.newY, ")")
		# if (addr not in ENEMIES):
		# 	ENEMIES.append(addr)

def sendGamePackets():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cX, cY = pygame.mouse.get_pos()
	packet = game_packet_pb2.GamePacket.MovePacket()
	packet.type = 3
	packet.player.name = player.get_name()
	packet.player.xPos = player.get_x()
	packet.player.yPos = player.get_y()
	packet.player.score = player.get_score()
	packet.player.image = player.get_image()
	packet.newX = cX
	packet.newY = cY
	sock.sendto(packet.SerializeToString(), ('192.168.0.74', 1218))

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


def startChat():
	global chatSocket, name, lobby_id

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

	game_loop()

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
	color_inactive = gray
	color_active = black
	color = color_inactive
	active = False
	text = 'Enter name here'
	done = False
	name = ''
	lobby_id = ''

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
						text = 'Enter lobby ID here'
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

		window.fill(background)
		window.blit(nameImg, (SCREEN_WIDTH/2-120, SCREEN_HEIGHT/2-125))		
		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Blit the text.
		window.blit(txt_surface, (input_box.x+5, input_box.y+5))

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

		window.fill(background)
		window.blit(lobbyImg, (SCREEN_WIDTH/2-120, SCREEN_HEIGHT/2-125))
		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Blit the text.
		window.blit(txt_surface, (input_box.x+5, input_box.y+5))

		pygame.display.flip()
		clock.tick(30)
	startChat()
#########################################################################################
def game_loop():
	pygame.mixer.music.play(-1)	
	global name, game_socket	
	x = (SCREEN_WIDTH * 0.45)
	y = (SCREEN_HEIGHT * 0.45)
	player = Player(name, x, y)
	
	font = pygame.font.Font(None, 25)
	clock = pygame.time.Clock()
	input_box = pygame.Rect(10, 600, 140, 25)
	color_inactive = pygame.Color(('gray'))
	color_active = pygame.Color('black')
	color = color_inactive
	active = False
	text = 'Enter message here'
	done = False

	player.daemon = True
	player.start()

	game_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	packet = game_packet_pb2.GamePacket.ConnectPacket()
	packet.type = 1
	packet.player.name = name
	packet.player.image = 1
	packet.update = game_packet_pb2.GamePacket.ConnectPacket.NEW
	packet.address = socket.gethostbyname(socket.gethostname())
	game_socket.sendto(packet.SerializeToString(), ('192.168.0.74', 1218))

	game_socket.close()

	gameThread = threading.Thread(target = gamePacketListener)
	gameThread.daemon = True
	gameThread.start()

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
		drawAdversaries()
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

		updateScoreBoard(player, name)

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
	global htppage
	global playerImg
	global playerImgInt

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
	if action == 6:
		if soundFlag == 1:
			pygame.mixer.music.play(-1)
			set_sound_flag(0)
		else:
			pygame.mixer.music.stop()
			set_sound_flag(1)
	if action == 7:
		htppage = 2
	if action == 8:
		htppage = 1
	if action == 10:
		choose_player_img()
	if action == 11:
		playerImgInt = 1
		playerImg = player1Img
		startGame()
		game_loop()
	if action == 12:
		playerImgInt = 2
		playerImg = player2Img
		startGame()
		game_loop()
	if action == 13:
		playerImgInt = 3
		playerImg = player3Img
		startGame()
		game_loop()

def set_sound_flag(switch):
	global soundFlag
	soundFlag = switch

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
	if htppage == 1:
		window.blit(htppgImg, (0, 0))
		menu_button(mouse, 1080, 470, 80, 80, 1080, 470, nextImg, anextImg, 7)	
	else:
		window.blit(htppg2Img, (0, 0))
		menu_button(mouse, 990, 470, 80, 80, 990, 470, prevImg, aprevImg, 8)	
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
	menu_button(mouse, 550, 350, 100, 50, 500, 350, playImg, aplayImg, 10)
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
