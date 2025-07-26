import pyautogui as pa
import time
pa.PAUSE = 1 # espera 1 seg. entre OPs

pa.press('win') # press -> pressionar tecla 
pa.write("chrome") # write -> escrever
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(2)
pa.click(x=582, y=114)
pa.write("lofi girl")
pa.press('ENTER')