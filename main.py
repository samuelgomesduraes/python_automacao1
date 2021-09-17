#objetivo criar um programa que abre um link com abiblioteca pyautogui
import pyautogui
import time
#esta chamando o pyautogui e o.press vai pressionar o botao windows
pyautogui.alert('o codigo sera executado so aperte em ok e aguarde')
pyautogui.press('winleft')
#aguarda 1 segundo antes de executar a proxima tarefa
time.sleep(2)
#escreve o nome do aplicativo desejado
pyautogui.write('microsoft edge')
time.sleep(2)
#o enter e apertado e abre o micosoft edge(navegador)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://youtube.com')
pyautogui.press('enter')