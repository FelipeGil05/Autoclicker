from config import mouse, toogle_key, keyboard
from pynput.keyboard import Listener
import time
import config
import gui
from tkinter import ACTIVE, DISABLED

def clicker(type_click, repetion, interval):
	while True:
		if (config.click_flag):
			mouse.click(type_click, repetion)
		time.sleep(interval)

def	toogle(key):
	if (key == toogle_key):
		if config.click_flag == False:
			gui.start_button.config(state=DISABLED)
			gui.stop_button.config(state=ACTIVE)
		else:
			gui.start_button.config(state=ACTIVE)
			gui.stop_button.config(state=DISABLED)
		config.click_flag = not config.click_flag

def on_release(key):
	if key == keyboard._Key.esc:
		return False

def start_keyboard_listener():
	listener = Listener(
	on_press=toogle,
	on_release=on_release)
	listener.start()