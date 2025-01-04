from pyray import *
from os.path import join as os

longcode = open(os("coding-project","code.txt"),"r").read()
longcode = longcode.split()
code = []
for word in longcode:
    for letter in word:
        code.append(letter)
for i in range(len(code)):
    code[i] = int(code[i])
    if not code[i] in range(8):
        raise ValueError("Values out of range 0-7")

variables = [0,0,0,0,0,0,0,0]
colorList = [BLACK,WHITE, RED,GREEN,DARKBLUE, YELLOW,VIOLET,SKYBLUE]
pointer = Vector2(0,0)

rects = {}

init_window(512,512,"Fantasy Console")

index = 0

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    if index < len(code):
        num = code[index]

        if num == 0:
            pointer.x = eval(f"0o{code[index+1]}{code[index+2]}")*8
            pointer.y = eval(f"0o{code[index+3]}{code[index+4]}")*8
            index += 4

        elif num == 1:
            rects[f"({pointer.x}, {pointer.y})"] = colorList[code[index+1]]
            index += 1

        elif num == 2:
            if (index+2) == 0:
                variables[index+1] = index+3
            if (index+2) == 1:
                variables[index+1] = variables[index+3]
            if (index+2) == 2:
                variables[index+1] = index+3
            index += 3

    for rect in rects:
       draw_rectangle(int(eval(rect)[0]),int(eval(rect)[1]),8,8,rects[rect])
    end_drawing()
    index += 1


close_window()