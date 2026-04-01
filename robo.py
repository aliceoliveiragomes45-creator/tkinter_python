import pyautogui
from time import sleep

pyautogui.click(1277,197, duration=1 )
pyautogui.press("enter")
sleep(3)
pyautogui.click(987,616, duration= 2)
pyautogui.write('8520789')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
#clicar em novo produtos
pyautogui.click(39,39, duration=1)
with open('itens.txt', 'r')as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]




        
       
        pyautogui.click(158,85,duration=1)
        pyautogui.write(id_prod)
        pyautogui.click(165,139, duration=1)
        pyautogui.write(nome)
        pyautogui.click(162,195, duration=1)
        pyautogui.write(qntd)
        pyautogui.click(160,250,duration=1)
        pyautogui.write(preco)
        sleep(2)
        pyautogui.write(211,291,duration=1)
        pyautogui.press('enter')



