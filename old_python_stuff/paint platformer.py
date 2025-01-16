import pyautogui as pyag
from keyboard import is_pressed as ip
level = [0,1]
jump = False
pos = {'x':250,'y':240,'v':0}
moves = {'a':'-20','d':'20'}
# minimize tabs then open paint
pyag.hotkey('win','d')
pyag.hotkey('win','r'); pyag.typewrite('mspaint'); pyag.press('enter')
pyag.sleep(0.2)
pyag.hotkey('win','up')
pyag.hotkey('ctrl','w'); pyag.press('right'); pyag.press('tab',3)
pyag.press('space')
pyag.hotkey('shift','tab'); pyag.typewrite('500')
pyag.hotkey('shift','tab'); pyag.typewrite('1000')
pyag.press('enter')

# draws screen then reset
def screen():
    pyag.PAUSE = 0.01
    pyag.click(422,64) # circle tool 
    pyag.moveTo(pos['x'],pos['y']) # creates player
    pyag.drag(-50,-50)
    pyag.sleep(0.2)
    #resets screen
    pyag.PAUSE = 0.1
    pyag.hotkey('ctrl','z')
def move():
    for i in range(2):
        if ip('ad'[i]):
            pos['x'] += int(moves['ad'[i]])
    if ip('w') and jump:
        pos['v'] += 40
def rect(rect):
    pass
pyag.alert(text='WAD to move\nhold Escape to leave\nmoving your mouse breaks the game\nif you can\'t quit move the mouse to a corner of your screen',title='Instructions',button='START')
while True:
    if level[0] != level[1]:
        rect('s') #make a list of a tuple of levels or vice versa (so its not repetitive and confusing)
        level[0] = level[1]
    screen()
    move()
    pos['y'] -= pos['v']
    if pos['y'] > 639:
        pos['y'] = 640
        jump = True
    else:
        pos['v'] -= 20
        jump = False
    if ip('esc'):
        break
if pyag.getActiveWindowTitle() != 'Program Manager':
    pyag.hotkey('alt','f4')
    pyag.press('right')
    pyag.press('enter')
pyag.alert('game quit','QUITTER','okay')
