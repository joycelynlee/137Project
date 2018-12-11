import game_player_pb2
import game_packet_pb2
import tcp_packet_pb2

# import pygame
import random

import socket
import threading
import os

global game_socket, chat_socket

HEIGHT = 650
WIDTH = 1200
FOOD = []
PLAYERS = []

# class Player(object):
#     def __init__(self, name):
#         self.name = name
#         self.x = random.randint(10, SCREEN_WIDTH-10)
#         self.y = random.randint(10, SCREEN_HEIGHT-10)
#         self.score = 0
#         # self.location = (x,y)
#         # self.destination = self.location
#         # self.stopDis = 5
#         self.img = pygame.transform.scale(playerImg, (40, 40))

#     def get_x(self):
#         return self.x

#     def get_y(self):
#         return self.y

#     def get_score(self):
#         return self.score

#     def get_level(self):
#         return self.score/10+1

#     def get_size(self):
#         return self.get_level()*10

#     def get_speed(self): #amount of time in ms it takes for player to move 100u
#         return self.get_size()/5

#     def get_img(self):
#         return self.img

#     def set_x(self, newX):
#         self.x = newX

#     def set_y(self, newY):
#         self.y = newY

#     def add_score(self):
#         self.score+=1

# class Food(object):
# 	def __init__(self):
# 		self.x = random.randint(10, SCREEN_WIDTH-10)
# 		self.y = random.randint(10, SCREEN_HEIGHT-10)
# 		self.pic = random.randint(1, 2)
# 		self.size = 10
# 		self.location = (self.x, self.y)

# 	def render(self, window):
# 		if self.pic == 1:
# 			displayImg = pygame.transform.scale(food1Img, (self.size, self.size))			
# 		if self.pic == 2:
# 			displayImg = pygame.transform.scale(food2Img, (self.size, self.size))			
# 		window.blit(displayImg, (self.x, self.y))


# #######################GAME BACKGROUND MECHANICS##########################
# def spawn_food(amountOfFood):
# 	+if(amountOfFood < 5):
# 		food = Food()
# 		FOOD.append(food)
# 		amountOfFood = amountOfFood + 1

# def collisionDetection():
#     for player in PLAYERS:
#         for item in FOOD:
#             if(getDistance((item.x, item.y), (player.x, player.y)-item.size) <= player.get_size()):
#                 player.add_score()
#                 FOOD.remove(item)
#     # for item in FOOD:
#     #     if(getDistance((item.x, item.y), (self.x, self.y)) <= ((self.size/1.8)+45)):
#     #         self.score += 1
#     #         FOOD.remove(item)
#     # for player in player_list:
#     #     if(getDistance((self.x, self.y), (player.x), (player.y)) <= ((self.size/1.8)+(player.size/1.8)):
#     #         if(self.score < player.score):
#     #             print('You Lose!')
# ##########################################################################

# def getDistance(pos1,pos2):
#     px,py = pos1
#     p2x,p2y = pos2
#     diffX = math.fabs(px-p2x)
#     diffY = math.fabs(py-p2y)

#     return ((diffX**2)+(diffY**2))**(0.5)

# def sendToAll(packet):
#         socket.send()

def move(player, xDst, yDst):
    smoothing = getDistance((player.get_x(), player.get_y()), (xDst, yDst))/player.get_speed()
    for i in range(smoothing):
        player.set_x((player.get_x() + xDst) / smoothing)
        player.set_y((player.get_y() + yDst) / smoothing)
        packet = game_packet_pb2.GamePacket.MovePacket()
        packet.player = player.name
        packet.x = player.get_x()
        packet.y = player.get_y()
        game_socket.send(packet.SerializeToString())

def addPlayer(name, addr, img):
    print(name + ' has connected successfully! (' + addr + ')')
    packet = game_packet_pb2.GamePacket.ConnectPacket()
    packet.type = 1
    packet.player.name = name
    packet.player.xPos = random.randint(10, WIDTH-10)
    packet.player.yPos = random.randint(10, HEIGHT-10)
    packet.player.score = 0
    packet.player.image = img
    packet.update = game_packet_pb2.GamePacket.ConnectPacket.SELF
    packet.address = addr
    game_socket.sendto(packet.SerializeToString(), (addr, 1218))
    PLAYERS.append(addr)

def packetListener():
    templog = ''
    while True:
        packet = game_packet_pb2.GamePacket()
        data = game_socket.recv(1024)
        data1 = data
        packet.ParseFromString(data1)
        if packet.type == game_packet_pb2.GamePacket.DISCONNECT:
            packet = game_packet_pb2.GamePacket.DisconnectPacket()
            packet.ParseFromString(data)
            if packet.update == 0:
                print(packet.player.name, " has disconnected!")
                templog.append(packet.player.name + " has disconnected!")
            elif packet.update == 1:
                print(packet.player.name, " has lost connection!")
                templog.append(packet.player.name + " has lost connection!")
        elif packet.type == game_packet_pb2.GamePacket.CONNECT:
            packet = game_packet_pb2.GamePacket.ConnectPacket()
            packet.ParseFromString(data)
            # player_list.add(packet.address)

            if packet.update == game_packet_pb2.GamePacket.ConnectPacket.NEW:
                addPlayer(packet.player.name, packet.address, packet.player.image)
            # print(packet.player.name + ' has connected successfully! ')
            # print(packet.player.name, " successfully connected to lobby ", packet.lobby_id)
            # templog.append(packet.player.name + " successfully connected to lobby " + packet.lobby_id)
        elif packet.type == game_packet_pb2.GamePacket.CREATE_LOBBY:
            packet = game_packet_pb2.GamePacket.CreateLobbyPacket()
            packet.ParseFromString(data)
            print("Lobby ", packet.lobby_id, " successfully created!")
            templog.append("Lobby " + packet.lobby_id + " successfully created!")
        elif packet.type == game_packet_pb2.GamePacket.CHAT:
            packet = game_packet_pb2.GamePacket.MovePacket()
            packet.ParseFromString(data)
            print(packet.player.name, " has moved to (", packet.newX, ", ", packet.newY, ")")
            # templog.append(packet.player.name + ": " + packet.message)
        elif packet.type == GamePacket.PacketType.PLAYER_LIST:
            packet = game_packet_pb2.GamePacket.PlayerListPacket()
            packet.ParseFromString(data)
            print(packet.player_list)
            templog.append(packet.player_list)
        elif packet.type == GamePacket.PacketType.END:
            packet = game_packet_pb2.GamePacket.EndPacket()
            packet.ParseFromString(data)
            print("Error: ", packet.err_message)
            templog.append("Error: " + packet.err_message)
        elif packet.type == GamePacket.PacketType.ERR_LFULL:
            packet = game_packet_pb2.GamePacket.ErrLfullPacket()
            packet.ParseFromString(data)
            print("Error: ", packet.err_message)
            templog.append("Error: " + packet.err_message)		
        elif packet.type == GamePacket.PacketType.ERR:
            packet = game_packet_pb2.GamePacket.ErrPacket()
            packet.ParseFromString(data)
            print("Error: ", packet.err_message)
            templog.append("Error: " + packet.err_message)

def main():
    global game_socket, chat_socket
    game_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    game_socket.bind((socket.gethostbyname(socket.gethostname()), 1218))
    print(socket.gethostbyname(socket.gethostname()))

    packetListenerThread = threading.Thread(target = packetListener)
    packetListenerThread.daemon = True
    packetListenerThread.start()

    chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    chat_socket.connect(('202.92.144.45', 80))

    packet = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
    packet.type = 2
    packet.max_players =  5
    chat_socket.send(packet.SerializeToString())
    data = chat_socket.recv(1024)
    packet.ParseFromString(data)
    lobby = packet.lobby_id

    print(lobby)

    player_list = []

    while True:
        continue

main()