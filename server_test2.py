import socket
import threading

PLAYERS = []

def packetListener():
    game_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    game_socket.bind((socket.gethostbyname(socket.gethostname()), 1218))
    while True:
        data, addr = game_socket.recv(4096)
        if(addr not in PLAYERS):
            PLAYERS.append(addr)
        for player in PLAYERS:
            game_socket.sendto(data, (player, 1218))

packetListener()