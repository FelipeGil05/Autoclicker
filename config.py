from pynput.mouse import Controller as Mouse_Controller
from pynput.keyboard import Controller as Keyboard_Controller
from pynput.mouse import Button

mouse = Mouse_Controller()
keyboard = Keyboard_Controller()

click_flag = False
toogle_key = keyboard._Key.f6
button_to_be_clicked = Button.left
repetions_per_iteration = 1
interval_between_clicks = 1