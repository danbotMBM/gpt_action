import pyautogui
import re
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

def parse_step(line):
    coords_pat = r'\{(.*?)\}'
    coords = re.findall(coords_pat, line)

    keyboard_pat = r'"(.*?)"'
    keys = re.findall(keyboard_pat, line)

    enter_pat = r'Enter key|enter key'
    enter = re.findall(enter_pat, line)

    print(coords, keys, enter)
    for c in coords:
        x, y = (int(i.strip()) for i in c.split(","))
        pyautogui.moveTo(x, y, duration=1)
        time.sleep(0.5)
        pyautogui.click(x, y)

    for k in keys:
        pyautogui.typewrite(k)

    if enter:
        pyautogui.press('enter')

    


with open("input.txt") as f:
    for line in f.readlines():
        #line = input()
        parse_step(line)
        time.sleep(1)