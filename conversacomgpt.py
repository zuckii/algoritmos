import pyautogui as pya
import time

print("Posicione-se! O script vai começar...")
time.sleep(1)

pya.hotkey('ctrl', 'alt', 't')
time.sleep(2) 

pya.write('google-chrome\n')
time.sleep(3)

pya.hotkey('tab')
time.sleep(1)

pya.hotkey('enter')
time.sleep(1)

pya.write('https://chatgpt.com/')
pya.hotkey('enter')
time.sleep(3)

pya.click(967, 720)
time.sleep(1)

pya.click(690, 513)
time.sleep(1)

pya.write('Faca uma pergunta utilizando somente uma frase de curiosidade geral', interval=0.05)
pya.hotkey('enter')
time.sleep(2)

for i in range(19):
    pya.hotkey('tab')
    time.sleep(0.1)

pya.hotkey('enter')

pya.click(34, 153)
time.sleep(1)

pya.hotkey('ctrl', 'v')
time.sleep(1)

pya.hotkey('enter')