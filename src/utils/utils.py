# utils.py
import sys
import os

# Default encode format
format = 'utf-8'

# Get arguments or use default
# ip: 127.0.0.1, port: 65432
def get_args():
  ip, port = '', None

  try:
    ip = sys.argv[1]
  except IndexError:
    ip = '127.0.0.1'
  try:
    port = int(sys.argv[2])
  except IndexError:
    port = 65432

  return ip, port

# Clear console depending on the operating system
def clear():
  os.system('cls' if os.name=='nt' else 'clear')