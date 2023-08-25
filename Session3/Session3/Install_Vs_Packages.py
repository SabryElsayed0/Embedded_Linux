import pyautogui
import time
import os
#############################################################################
def Searh_On_Screen(image):
    # my_pass = os.path.dirname(os.path.realpath(__file__))+"/"+image
    install_icon = None
    while install_icon is None:
        install_icon = pyautogui.locateOnScreen(image,confidence=0.9)
    install_center = pyautogui.center(install_icon)
    pyautogui.click(install_center)
    time.sleep(2)
    
def Open_Search(name):
    pyautogui.hotkey('ctrl' , 'shift' , 'X')
    time.sleep(1)
    pyautogui.keyDown('backspace')
    time.sleep(1)
    pyautogui.keyUp('backspace')
    time.sleep(1)
    pyautogui.write(name)
    time.sleep(2)
    
    
pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('vs')
time.sleep(1)

print(__file__)
Searh_On_Screen("VsCode.png")
pyautogui.hotkey('enter')
time.sleep(2)
Open_Search("clangd")
Searh_On_Screen("clangd.png")
pyautogui.hotkey('enter')
time.sleep(1)
Searh_On_Screen("install.png")
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

Open_Search("C++ testmate")
time.sleep(2)
Searh_On_Screen("C++_testmate.png")
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(1)
Searh_On_Screen("install.png")
pyautogui.hotkey('enter')
print("i found the install")
time.sleep(1)
