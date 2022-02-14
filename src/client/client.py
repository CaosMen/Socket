# client.py
import socket
import sys

from consolemenu import *
from consolemenu.items import *

# utils.py
sys.path.append('../utils')
from utils import get_args
from utils import clear

# Room operations
from room import create_room
from room import enter_room

# Create username
def create_username(ip, port):
  local_user = ''
  while len(local_user) < 3:
    clear()

    print(f'Client successfully connected to server at {ip}:{port}')
    local_user = input('Enter your username (at least three characters): ')
  
  return local_user

# Create Menu
def create_menu(server, username):
  menu = ConsoleMenu('Local Chat', 'Use the application to connect and chat with people in your local network')

  create_item = FunctionItem('Create room', create_room, args=[server, username])
  enter_item = FunctionItem('Enter room', enter_room, args=[server, username])

  menu.append_item(create_item)
  menu.append_item(enter_item)

  return menu

# Main
def main():
  # Get args from console or use default
  ip, port = get_args()
  
  # Connecting to the server
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
  except socket.error:
    print('Failed to connect socket!')
    return

  # Ser username
  username = create_username(ip, port)
  
  # Creating and showing the menu
  menu = create_menu(server, username)
  menu.show()

  server.close()

if __name__ == '__main__':
  main()