import game_packet_pb2

import socket
import threading
import os

game_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# game_socket.bind(('192.168.0.74', 1218))

packet = game_packet_pb2.GamePacket.ConnectPacket()
packet.type = 1
packet.player.name = input('Enter name: ')
packet.player.image = 1
packet.update = game_packet_pb2.GamePacket.ConnectPacket.NEW
packet.address = socket.gethostbyname(socket.gethostname())
game_socket.sendto(packet.SerializeToString(), ('192.168.0.74', 1218))

while True:
    data = game_socket.recvfrom(1024, '192.168.0.74')
    packet = game_packet_pb2.GamePacket.ConnectPacket()
    packet.ParseFromString(data)
    print(packet.player.name)