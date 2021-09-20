import keyboard
import time
import pygetwindow as gw


try:  
        while(True):
                try:
                        notepadWindow = gw.getWindowsWithTitle('Salvar como')[0]
                        notepadWindow.restore()
                        notepadWindow.activate()
                        notepadWindow.activate()
                        keyboard.press('enter')
                        time.sleep(1)
                except :
                        print('Não esta aberto')
                        time.sleep(0.2)
except KeyboardInterrupt:
        pass
