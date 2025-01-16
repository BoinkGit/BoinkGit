import turtle
import pyautogui as pyag
turtle.Screen()
center = (pyag.size()[0]/2,pyag.size()[1]/2)
pyag.moveTo(center)
'''while True:
    pos = pyag.position()
    turtle.goto(pos[0]-center[0],-1*(pos[1]-center[1]))
    turtle.onkey()'''
def fax():
    print(True)
turtle.onkey(fax,'space')
while True:
    turtle.listen()