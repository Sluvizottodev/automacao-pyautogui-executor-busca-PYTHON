import pyautogui
import time
import os

os.system("Start bloco de notas")
time.sleep(1)

pyautogui.write("Olá, mundo!", interval=0.05)
time.sleep(0.5)

pyautogui.hotkey("ctrl", "s")
time.sleep(0.5)

pyautogui.write("ex_automacao_notas_py.txt")
pyautogui.press("enter")