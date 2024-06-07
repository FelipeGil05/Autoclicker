import tkinter as tk
from pynput.mouse import Button
import config

LEFT_CLICK = "Left"
RIGHT_CLICK = "Right"
MIDDLE_CLICK = "Middle"

def button_start_toogle():
	global start_button, stop_button
	config.click_flag = not config.click_flag
	start_button.config(state=tk.DISABLED)
	stop_button.config(state=tk.ACTIVE)

def button_stop_toogle():
	global start_button, stop_button
	config.click_flag = not config.click_flag
	start_button.config(state=tk.ACTIVE)
	stop_button.config(state=tk.DISABLED)

def	update_delay():
	config.interval_between_clicks = float(interval_entry.get())
	print(config.interval_between_clicks)

def on_interval_entry_update(event):
	try:
		update_delay()
	except ValueError:
		pass

def update_click_type(type):
	if (type == LEFT_CLICK):
		config.button_to_be_clicked = Button.left
	elif (type == RIGHT_CLICK):
		config.button_to_be_clicked = Button.right
	else:
		config.button_to_be_clicked = Button.middle


gui = tk.Tk()
gui.title("Auto Clicker")

frame = tk.Frame(gui)
frame.pack(padx=10, pady=10)

interval_label = tk.Label(frame, text="Click Interval (seconds):")
interval_label.grid(row=0, column=0, padx=5, pady=5)

interval_entry = tk.Spinbox(frame, from_=0.001, to=100, increment=0.001, command=update_delay)
interval_entry.delete(0, "end")
interval_entry.insert(0, "1")
interval_entry.bind("<KeyRelease>", on_interval_entry_update)
interval_entry.grid(row=0, column=1, padx=5, pady=5)

selected_option = tk.StringVar(gui)
selected_option.set(LEFT_CLICK)
options = [LEFT_CLICK, RIGHT_CLICK, MIDDLE_CLICK]
click_types = tk.OptionMenu(frame, selected_option, *options, command=update_click_type)
click_types.grid(row=1, column=1 , padx=20, pady=20)

start_button = tk.Button(frame, text="Start", command=button_start_toogle)
start_button.grid(row=2, column=0, padx=5, pady=5)

stop_button = tk.Button(frame, text="Stop", command=button_stop_toogle, state=tk.DISABLED)
stop_button.grid(row=2, column=1, padx=5, pady=5)
