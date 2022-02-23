# room.py
import sys

# utils.py
sys.path.append('../utils')
from utils import format

# Return key of connection room
def get_user_room(rooms, connec):
  for key in rooms.keys():
    if connec in rooms[key]:
      return key

  return -1

# Send message for every user in room
def message_room(rooms, connec, addr):
  recv = connec.recv(2048)
  message = recv.decode(format)
  
  key = get_user_room(rooms, connec)

  for current_connec in rooms[key]:
    # Sends the message to everyone except the sender
    if current_connec != connec:
      current_connec.send('MSG'.encode(format))
      current_connec.send(message.encode(format))

# Connect in a room
def connect_room(rooms, connec, addr):
  recv = connec.recv(2048)
  connect_data = recv.decode(format)

  room_name, username = connect_data.split('|')[0], connect_data.split('|')[1]

  rooms[room_name].append(connec)

  for current_connec in rooms[room_name]:
    # Sends the message to everyone except the sender
    if current_connec != connec:
      current_connec.send('MSG'.encode(format))
      current_connec.send(f'|Server| The user {username} connected in the room'.encode(format))

  print(f'The IP owner {addr[0]} with the username {username} has just logged into the room: {room_name}\n')

# Create a room
def create_room(rooms, connec, addr):
  while True: 
    try:
      recv = connec.recv(2048)

      if not recv:
        break

      room_name = recv.decode(format)

      if room_name == '/exit':
        break
      else:
        if room_name in rooms:
          # Send the value '0' to show that a room with that name already exists
          connec.send('0'.encode(format))
        else:
          # Sends the value '0' to show that the room can be created
          connec.send('1'.encode(format))
          # Create room
          rooms[room_name] = []
          print(f'The IP owner {addr[0]} created the room: {room_name}')
          break
    except Exception as err:
      print(f'The IP owner {addr[0]} had an exception')
      print(f'{err}\n')
      break

# Enter a room
def enter_room(rooms, connec, addr):
  while True: 
    try:
      recv = connec.recv(2048)

      if not recv:
        break

      room_name = recv.decode(format)

      if room_name == '/exit':
        break
      else:
        if room_name in rooms:
          # Sends the value '1' to show that the room exists
          connec.send('1'.encode(format))
          break
        else:
          # Sends the value '0' to show that the room not exists
          connec.send('0'.encode(format))
    except Exception as err:
      print(f'The IP owner {addr[0]} had an exception')
      print(f'{err}\n')
      break

# Leave a room
def leave_room(rooms, connec, addr):
  # User room
  key = get_user_room(rooms, connec)
  
  if key != -1:
    # Remove user from room
    if connec in rooms[key]:
      rooms[key].remove(connec)

    # Check if room is empty to delete
    if len(rooms[key]) == 0:
      del rooms[key]
    
    # Send command to exit "handle_message" thread
    connec.send('EXT'.encode(format))