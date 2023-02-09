import pygetwindow as gw
import pyautogui
import time
print("É necessário estar com o arquivo dsvagua.dat aberto selecionado o primeiro campo da primeira linha de ano e teclado no modo insert no notepad++")
#print(gw.getAllTitles())
inp_posto =input('Digite o número de postos (ciclos a serem feito) (dica contar o número de anos): ')
n_posto=int(inp_posto)
gw.getWindowsWithTitle('C:\\Users\\Televisão\\Energizou Dropbox\\2 Mesa\\Middle\\Modelos CEPEL\\Decks\\Encadeados\\5. Encadeado MMGD-2024\\NW202401\\dsvagua.dat - Notepad++')[0].activate()

def ciclo():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    with pyautogui.hold('shiftright'):
        with pyautogui.hold('shiftleft'):
            pyautogui.press('right', presses=103)
    pyautogui.hotkey('ctrlleft', 'c')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrlleft', 'v')
    pyautogui.press('up')
    pyautogui.press('right', presses=4)
    pyautogui.write('8')
    pyautogui.press('down')
    pyautogui.press('left', presses=4)

for i in range(n_posto):
    ciclo()

