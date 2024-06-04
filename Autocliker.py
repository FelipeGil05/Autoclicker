from clicker import start_keyboard_listener, clicker
from config import button_to_be_clicked, repetions_per_iteration, interval_between_clicks
import threading
from gui import gui

def main():
	click_thread = threading.Thread(target=clicker, args=(button_to_be_clicked, repetions_per_iteration, interval_between_clicks))
	click_thread.daemon = True
	click_thread.start()

	start_keyboard_listener()
	gui.mainloop()

try:
	main()
except KeyboardInterrupt:
	print("Exiting...")