import cv2
import numpy as np
import win32api
import win32con
import keyboard
import pyautogui
import time 


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# Load the template image
template = cv2.imread('aa.png', cv2.IMREAD_GRAYSCALE)

while not keyboard.is_pressed('q'):
    # Take a screenshot
    screenshot = pyautogui.screenshot(region=(0, 150, 380, 250))

    # Convert the screenshot to grayscale
    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Apply template matching
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    # Find the maximum value in the result matrix
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the maximum value is above a certain threshold, consider it a match
    if max_val > 0.5:
        x, y = max_loc
        click(x+20 , y+170 )
