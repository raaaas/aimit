import cv2
import numpy as np
import win32api
import win32con
import keyboard
import pyautogui
import time

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Load the template images
template_aa = cv2.imread('aa.png', cv2.IMREAD_COLOR)
template_bbb = cv2.imread('bomb0.png', cv2.IMREAD_GRAYSCALE)
template_play = cv2.imread('play.png', cv2.IMREAD_GRAYSCALE)

while not keyboard.is_pressed('q'):
    # Take a screenshot
    screenshot = pyautogui.screenshot(region=(0, 150, 380, 280))

    # Convert the screenshot to grayscale
    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Apply template matching for 'aa' template
    #result_aa = cv2.matchTemplate(gray, template_aa, cv2.TM_CCOEFF_NORMED)
    result_aa = cv2.matchTemplate(cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR), template_aa, cv2.TM_CCOEFF_NORMED)

    # Find the maximum value in the result matrix
    min_val_aa, max_val_aa, min_loc_aa, max_loc_aa = cv2.minMaxLoc(result_aa)

    # Check if the maximum value is above a certain threshold
    if max_val_aa > 0.5:
        x, y = max_loc_aa
        click(x+20, y+180)

"""         # Apply template matching for 'bbb' template
        result_bbb = cv2.matchTemplate(gray, template_bbb, cv2.TM_CCOEFF_NORMED)

        # Find the maximum value in the result matrix
        min_val_bbb, max_val_bbb, min_loc_bbb, max_loc_bbb = cv2.minMaxLoc(result_bbb)

        # If the maximum value is above a certain threshold, ignore the match
        if max_val_bbb < 0.3:  # adjust this value based on your needs
            click(x+20, y+180) """
