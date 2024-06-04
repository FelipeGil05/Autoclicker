import tkinter as tk
from config	import click_flag
import config

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


gui = tk.Tk()
gui.title("Auto Clicker")

frame = tk.Frame(gui)
frame.pack(padx=10, pady=10)

interval_label = tk.Label(frame, text="Click Interval (seconds):")
interval_label.grid(row=0, column=0, padx=5, pady=5)

interval_entry = tk.Entry(frame)
interval_entry.grid(row=0, column=1, padx=5, pady=5)
interval_entry.insert(0, "0.01")

start_button = tk.Button(frame, text="Start", command=button_start_toogle)
start_button.grid(row=1, column=0, padx=5, pady=5)

stop_button = tk.Button(frame, text="Stop", command=button_stop_toogle, state=tk.DISABLED)
stop_button.grid(row=1, column=1, padx=5, pady=5)
