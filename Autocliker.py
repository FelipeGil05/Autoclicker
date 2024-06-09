from clicker import start_keyboard_listener, clicker
import threading
from gui import gui

def main():
	click_thread = threading.Thread(target=clicker)
	click_thread.daemon = True
	click_thread.start()

	start_keyboard_listener()
	gui.mainloop()

try:
	main()
except KeyboardInterrupt:
	pass