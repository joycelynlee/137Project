# 137Project - AGARIO

AGARIO, a remake of the Agar.io game, is a multiplayer game written in Python that uses TCP for in-game chat and UDP as a game server.

## Installation
### Linux
1. Make sure that your computer has Python 3 installed by typing ```python3 --version```

2. Use the package manager pip to install pygame.```pip install pygame```
3. Make sure to have protobuf for Python installed. There are installation instruction on Google Protobuf's Github repository here: https://github.com/protocolbuffers/protobuf/tree/master/python

## Usage
First, run server.py. This will generate a lobby code that the players will use to enter the lobby.
```bash
python3 server.py
```
Then run client.py
```bash
python3 client.py
```
Players that want to join must run client.py

## How to play
### Start a game
To join a game room, you must enter your name and the lobby code.
### Games rules
To win, you must consume food that will appear. The number of food is limited and when there are no more food left to be consumed, the player with the biggest size and highest score will be the winner.
### Controls
Use your mouse to control your avatar.
