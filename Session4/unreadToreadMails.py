# Using “Pyautogui” to open Emails and change Emails from unread to read
import pyautogui
import time
import os



pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('gmail')
time.sleep(1)
print(__file__)
my_pass = os.path.dirname(os.path.realpath(__file__))+"/gmail.png"

isfind = None
while isfind is None:
    isfind = pyautogui.locateAllOnScreen(my_pass,confidence=0.7)

# print("i get the path")
pyautogui.hotkey('enter')
time.sleep(1)
###########################################################################
# my_pass = os.path.dirname(os.path.realpath(__file__))+"/clangd.png"
search_icon = None
while search_icon is None:
    search_icon = pyautogui.locateOnScreen("SearchBar.png",confidence=0.9)
search_center = pyautogui.center(search_icon)
pyautogui.click(search_center)
time.sleep(1)
pyautogui.write('is:unread ')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

###########################################################################
# my_pass = os.path.dirname(os.path.realpath(__file__))+"/clangd.png"
selectall_icon = None
while selectall_icon is None:
    selectall_icon = pyautogui.locateOnScreen("selectall.png",confidence=0.9)
selectall_center = pyautogui.center(selectall_icon)
pyautogui.click(selectall_center)
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

###########################################################################
# my_pass = os.path.dirname(os.path.realpath(__file__))+"/clangd.png"
select_icon = None
while select_icon is None:
    select_icon = pyautogui.locateOnScreen("select.png",confidence=0.9)
select_center = pyautogui.center(select_icon)
pyautogui.click(select_center)
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

###########################################################################
# my_pass = os.path.dirname(os.path.realpath(__file__))+"/clangd.png"
markasread_icon = None
while markasread_icon is None:
    markasread_icon = pyautogui.locateOnScreen("markasread.png",confidence=0.9)
markasread_center = pyautogui.center(markasread_icon)
pyautogui.click(markasread_center)
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

# pyautogui.hotkey('enter')
# print("i found the path")
# time.sleep(1)
# ###############################################################################
# my_pass = os.path.dirname(os.path.realpath(__file__))+"/install.png"
# install_icon = None
# while install_icon is None:
#      install_icon = pyautogui.locateOnScreen("install.png",confidence=0.9)

# install_center = pyautogui.center(install_icon)
# pyautogui.click(install_center)
# time.sleep(1)
# pyautogui.hotkey('enter')
# print("i found the install")
# time.sleep(1)