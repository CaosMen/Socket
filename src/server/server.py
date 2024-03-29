# server.py
import socket
import sys

from threading import Thread

# utils.py
sys.path.append('../utils')
from utils import get_args
from utils import clear
from utils import format

# Room operations
from room import message_room
from room import connect_room
from room import create_room
from room import enter_room
from room import leave_room

# Global clients list
list_clients = []
# Global rooms list
rooms = {}

# Disconnect client
def disconnect_client(connec, addr):
  if connec in list_clients:
    list_clients.remove(connec)
    leave_room(rooms, connec, addr)

# Client thread
def client_thread(connec, addr):
  # Commands allowed
  commands = {
    'MSG': message_room,
    'CNC': connect_room,
    'CTR': create_room,
    'ETR': enter_room,
    'EXT': leave_room
  }

  while True:
    try: 
      recv = connec.recv(3)
    
      if not recv:
        break
      
      message = recv.decode(format)
      commands.get(message)(rooms, connec, addr)
    except Exception as err:
      print(f'The IP owner {addr[0]} had an exception')
      print(f'{err}\n')
      break
  
  disconnect_client(connec, addr)
  connec.close()

# Main
def main():
  # Get args from console or use default
  ip, port = get_args()
  
  # Creating server
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((ip, port))
    server.listen()
  except socket.error as err:
    print('Failed to create socket!')
    print(f'{err}\n')
    return

  # Server is on
  clear()
  print(f'The server was started at {ip}:{port}\n')
  
  # Loop for accept new connections
  while True: 
    connec, addr = server.accept()

    list_clients.append(connec)

    print(f'The IP owner {addr[0]} just logged in!')
    print(f'Total connected users: {len(list_clients)}\n')

    thread = Thread(target=client_thread, args=(connec, addr))
    thread.start()

if __name__ == '__main__':
  main()