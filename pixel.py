import pyautogui
import time

print("Mova o mouse para a posição desejada. A coordenada será mostrada em 5 segundos...")
time.sleep(5)

x, y = pyautogui.position()
print(f"A coordenada atual do mouse é: ({x}, {y})")