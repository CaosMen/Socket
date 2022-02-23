# chat.py
import sys

from threading import Thread

from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import SearchToolbar, TextArea
from prompt_toolkit.key_binding.bindings.page_navigation import scroll_page_up, scroll_page_down

# utils.py
sys.path.append('../utils')
from utils import format

# Create room container
def create_container(help_text):
  # Creating input field and output
  search_field = SearchToolbar()

  output_field = TextArea(style='class:output-field', text=help_text)
  input_field = TextArea(
    height=1,
    prompt='>>> ',
    style='class:input-field',
    multiline=False,
    wrap_lines=False,
    search_field=search_field
  )

  # Split screen for input and output
  container = HSplit(
    [
      output_field,
      Window(height=1, char='.', style='class:line'),
      input_field,
      search_field,
    ]
  )

  return input_field, output_field, container

# Create room shortcuts
def create_keybindings(output_field):
  # The key bindings
  key_bindings = KeyBindings()

  # Exit
  @key_bindings.add('c-c')
  def _(event):
    event.app.exit()

  # Scroll Up
  @key_bindings.add('pageup')
  def _(event):
    w = event.app.layout.current_window
    event.app.layout.focus(output_field.window)
    scroll_page_up(event)
    event.app.layout.focus(w)

  # Scroll Down
  @key_bindings.add('pagedown')
  def _(event):
    w = event.app.layout.current_window
    event.app.layout.focus(output_field.window)
    scroll_page_down(event)
    event.app.layout.focus(w)

  return key_bindings

def handle_message(server, output_field):
  while True:
    try:
      recv = server.recv(3)

      if not recv:
        break
      
      identifier = recv.decode(format)
      
      if (identifier == 'MSG'):
        recv_msg = server.recv(2048)
        message = recv_msg.decode(format)

        new_text = output_field.text + f'{message}\n'

        output_field.buffer.document = Document(
          text=new_text, cursor_position=len(new_text)
        )
      elif (identifier == 'EXT'):
        break
      else:
        break
    except Exception as err:
      print(f'An exception error has occurred')
      print(f'{err}\n')
      break

# Create chat ui
def create_chat(server, room_name, username):
  # Initial text
  welcome_text = f'Welcome to the chat room {room_name}.'
  commands_text = 'Commands: Control-C (exit), Page Up (scroll up chat) and Page Down (scroll down chat).'
  help_text = f'{welcome_text}\n{commands_text}\n\n'

  input_field, output_field, container = create_container(help_text)

  # Handle sent messages
  def send_message(buff):
    text = f'<Me> {input_field.text}\n'
    new_text = output_field.text + text

    # Send text to server
    server.send('MSG'.encode(format))
    server.send(f'<{username}> {input_field.text}'.encode(format))

    # Add text to output buffer
    output_field.buffer.document = Document(
      text=new_text, cursor_position=len(new_text)
    )

  input_field.accept_handler = send_message

  key_bindings = create_keybindings(output_field)

  # Run application.
  application = Application(
    layout=Layout(container, focused_element=input_field),
    key_bindings=key_bindings,
    mouse_support=True,
    full_screen=True,
  )

  Thread(target=handle_message, args=(server, output_field)).start()

  application.run()