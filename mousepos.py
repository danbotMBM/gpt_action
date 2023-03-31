import pyautogui

while True:
    # Get and print the current mouse coordinates
    x, y = pyautogui.position()
    print('Mouse position:', x, y)
