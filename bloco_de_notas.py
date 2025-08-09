# -*- coding: utf-8 -*-
import pyautogui
import time
import os
import pyperclip

os.system("Start notepad")
time.sleep(1)

pyperclip.copy("Olá, mundo!")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.hotkey("ctrl", "s")
time.sleep(0.5)

pyautogui.write("ex_automacao_notas_py.txt")
pyautogui.press("enter")