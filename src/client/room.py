# room.py
import sys

# utils.py
sys.path.append('../utils')
from utils import clear
from utils import format

# Chat UI
from chat import create_chat

# Connecting in the room
def connect_room(server, room_name, username):
  # Send command to server
  server.send('CNC'.encode(format))
  server.send(f'{room_name}|{username}'.encode(format))

  # Run apliccation
  create_chat(server, room_name, username)

  # Called when leave room
  server.send('EXT'.encode(format))

# Create room
def create_room(server, username):
  # Send command to server
  server.send('CTR'.encode(format))

  # Room name set
  exit, tempted, valid = False, False, False
  room_name = ''
  while not valid:
    room_name = ''
    while len(room_name) < 3:
      clear()

      if tempted:
        print('A room with the given name already exists\n')

      print('To exit this screen type: /exit')
      room_name = input('Enter room name (at least three characters): ')
    
    tempted = True
    server.send(room_name.encode(format))

    if room_name == '/exit':
      exit = True
      break
    else:
      # Check if the room already exists
      response = server.recv(1)
      valid = bool(int(response.decode(format)))
  
  # Log into the room after creating
  if not exit:
    connect_room(server, room_name, username)

# Enter room
def enter_room(server, username):
  # Send command to server
  server.send('ETR'.encode(format))
  
  # Room enter
  exit, tempted, valid = False, False, False
  room_name = ''
  while not valid:
    room_name = ''
    while len(room_name) < 3:
      clear()

      if tempted:
        print('This room does not exist\n')

      print('To exit this screen type: /exit')
      room_name = input('Enter room name: ')
    
    tempted = True
    server.send(room_name.encode(format))

    if room_name == '/exit':
      exit = True
      break
    else:
      # Check if the room exists
      response = server.recv(1)
      valid = bool(int(response.decode(format)))

  # Log into the room after creating
  if not exit:
    connect_room(server, room_name, username)