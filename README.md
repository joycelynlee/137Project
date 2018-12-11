# 137Project - AGARIO

Title is a multiplayer Python game that uses TCP for in-game chat and UDP as a game server.

## Installation
Use the package manager pip to install AGARIO.
```bash
pip install pygame
```
Make sure to have protobuf for Python installed. There are installation instruction on Google Protobuf's Github repository here: https://github.com/protocolbuffers/protobuf/tree/master/python

## Usage
First, run server.py. This will generate a lobby code that the players will use to enter the lobby.
```bash
python3 server.py <arg1> <arg2>
```

Then run client.py
```bash
python3 client.py <arg1> <arg2>
```
Players can join the room by also running client.py.
Joining players must know the IP Address of the host(?).

## Game Instructions and Mechanics
1. To join a game room, you must enter your name and the lobby code.
2. To win, you must consume all of the food that will appear. Your avatar will increase in size and
