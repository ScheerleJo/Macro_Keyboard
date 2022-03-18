from pynput.keyboard import Key, Controller

keyboard = Controller()

def keyStroke(key:str):
    """A Function to simplyfy a standard Keystroke"""
    keyboard.press(key)
    keyboard.release(key)

keyStroke('9')