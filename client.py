#########################################
# REFERENCE/s:
# https://github.com/warna720/Simple-chat-server
#
#########################################

import socket, select, sys, cPickle, chat_pb2

chat_details = chat_pb2.join()
chat_details.nick = raw_input("Enter name: ")
chat_details.channel = raw_input("Choose channel: ")

server = "10.0.5.31"
port = 1080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((server, port))
except:
	print("ERROR! Could not connect!")

def send_data(sock, data):
	sock.send(cPickle.dumps(data))

def recv_data(sock):
	return cPickle.loads(sock.recv(4096))


send_data(s, ("join", chat_details))

while True:
    socket_list = [sys.stdin, s]
    
    #Ignoring write and error sockets. 
    read_sockets, _, _ = select.select(socket_list, [], [])
    
    for sock in read_sockets:
        #Incoming message from server
        if sock == s:
            data = recv_data(sock)
            
            if not data:
                sys.stdout.write("Disconnecting from server")
                exit()
                
            elif (data[0] == "error"):
                sys.stdout.write("Error: " + data[1].text)
                exit();
                
            elif (data[0] == "message"):
                sys.stdout.write(data[1].text)
                
        #User pressed enter
        else:
            msg = chat_pb2.message()
            msg.text = sys.stdin.readline().decode('utf-8')
            send_data(s, ("message", msg))