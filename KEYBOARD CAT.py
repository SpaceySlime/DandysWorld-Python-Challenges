# Roblox Automatic Player
from pynput.keyboard import Key, Controller
import pyautogui
import random
import time
Keyboard = Controller()

pyautogui.screenshot("Test.png", region= [0, 0, 1920, 1080])

Keys = [] #Bias forwards, duh.
convertstring = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
Keys = convertstring.split()

def PressKey(KeyCode, Time):
    Keyboard.press(KeyCode,)
    time.sleep(Time)
    Keyboard.release(KeyCode)

def Chat(Text):
    PressKey("/", 0.1)
    Keyboard.type(Text)
    time.sleep(0.1)
    PressKey(Key.enter, 0.1)

Chat("Powered by keyboard tapping robot")

while True:
    time.sleep(0.5)
    PressKey(random.choice(Keys), 1)