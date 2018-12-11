import player_pb2
import tcp_packet_pb2

import socket
import threading
import os

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

FOOD = []
PLAYERS = []

game_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
game_socket.bind((socket.gethostbyname(socket.gethostname()), 1218))
# game_socket.bind(('127.0.0.1', 12180))
# game_socket.listen(5)
print(socket.gethostbyname(socket.gethostname()))

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
    # c, a = game_socket.accept()
    # player_list.append(c)

    data = game_socket.recvfrom(1024)

    for addr in player_list:
        addr.send(data)




def packetListener():
    while True:
		packet = game_packet_pb2.GamePacket()
		data = chatSocket.recv(1024)
		data1 = data
		packet.ParseFromString(data1)
		if packet.type == GamePacket.PacketType.DISCONNECT:
			packet = game_packet_pb2.GamePacket.DisconnectPacket()
			packet.ParseFromString(data)
			if packet.update == 0:
				print(packet.player.name, " has disconnected!")
				templog.append(packet.player.name + " has disconnected!")
			elif packet.update == 1:
				print(packet.player.name, " has lost connection!")
				templog.append(packet.player.name + " has lost connection!")
		elif packet.type == GamePacket.PacketType.CONNECT:
			packet = game_packet_pb2.GamePacket.ConnectPacket()
			packet.ParseFromString(data)
            player_list.add(packet.address)
			# print(packet.player.name, " successfully connected to lobby ", packet.lobby_id)
			# templog.append(packet.player.name + " successfully connected to lobby " + packet.lobby_id)
		elif packet.type == GamePacket.PacketType.CREATE_LOBBY:
			packet = game_packet_pb2.GamePacket.CreateLobbyPacket()
			packet.ParseFromString(data)
			print("Lobby ", packet.lobby_id, " successfully created!")
			templog.append("Lobby " + packet.lobby_id + " successfully created!")
		elif packet.type == GamePacket.PacketType.CHAT:
			packet = game_packet_pb2.GamePacket.ChatPacket()
			packet.ParseFromString(data)
			print(packet.player.name, ": ", packet.message)
			templog.append(packet.player.name + ": " + packet.message)
		elif packet.type == GamePacket.PacketType.PLAYER_LIST:
			packet = game_packet_pb2.GamePacket.PlayerListPacket()
			packet.ParseFromString(data)
			print(packet.player_list)
			templog.append(packet.player_list)
		elif packet.type == GamePacket.PacketType.ERR_LDNE:
			packet = game_packet_pb2.GamePacket.ErrLdnePacket()
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
		updateChatLog(templog)