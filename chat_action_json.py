import json
import pyautogui
import re
import time


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

def parse_step(instr):
    print(instr)

    if "wait" in instr:
        time.sleep(instr["wait"])
        
    if "click" in instr:
        x, y = instr["click"]
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(2)
        pyautogui.click(x, y)

    if "type" in instr:
        pyautogui.typewrite(instr["type"])

    if "enter" in instr:
        pyautogui.press('enter')

    


with open("input.json") as f:
    instructions = json.load(f)
    for i in instructions:
        parse_step(i)