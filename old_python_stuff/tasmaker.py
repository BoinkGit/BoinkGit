from pyautogui import hotkey, typewrite, click, moveRel, moveTo
from keyboard import is_pressed, read_key
rswitch = 0
def keyList(keys):
    index = 0
    while index < len(keys):
        if keys[index][0] != "&" or len(keys[index]) < 2 :
            typewrite(keys[index])
        elif keys[index][0:3] == "&mx":
            moveRel(int(keys[index][3:len(keys[index])]),0)
        elif keys[index][0:3] == "&my":
            moveRel(0,(keys[index][3:len(keys[index])]))
        elif keys[index][0:2] == "&c":
            click()
        elif keys[index][0:2] == "&&":
            hotkey(keys[index][2:len(keys[index])])
        index += 1
print('done')
keys1 = ['&mx300','&my-300','&c','&c','&c','where','[space]','are','[space]','the','[space]','chickens','&mx-500','&my300','&c']
input()
keyList(keys1)
while True:
    if read_key() == "shift" and read_key == "r" and rswitch == 0: rswitch = 1
    elif read_key() == "ctrl" and read_key == "r" and rswitch == 1: rswitch = 0
    print(rswitch)
