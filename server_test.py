import socket
import threading
import tcp_packet_pb2

PLAYERS = []

def packetListener():
    recv_socket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_socket.bind((socket.gethostbyname(socket.gethostname()), 1218))
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    chat_socket.connect(('202.92.144.45', 80))

    packet = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
    packet.type = 2
    packet.max_players =  5
    chat_socket.send(packet.SerializeToString())
    data = chat_socket.recv(1024)
    packet.ParseFromString(data)
    lobby = packet.lobby_id

    print(socket.gethostbyname(socket.gethostname()))
    print(lobby)
    while True:
        data, addr = recv_socket.recvfrom(1024)
        if(addr not in PLAYERS):
            PLAYERS.append(addr)
        for player in PLAYERS:
            send_socket.sendto(data, (player[0], 1219))

packetListener()
