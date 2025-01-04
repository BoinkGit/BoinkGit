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

variables = [0,0,0,0,0,0,0,0]
colorList = [BLACK,WHITE, RED,GREEN,DARKBLUE, YELLOW,VIOLET,SKYBLUE]
pointer = Vector2(0,0)

rects = []

init_window(512,512,"Fantasy Console")

index = 0

while not window_should_close():
    begin_drawing()
    if index < len(code):
        num = code[index]

        if num == 0:
            pointer.x = eval(f"0o{code[index+1]}{code[index+2]}")*8
            pointer.y = eval(f"0o{code[index+3]}{code[index+4]}")*8
            index += 4

        if num == 1:
            a = f"draw_rectangle_v(Vector2({pointer.x},{pointer.y}),Vector2(8,8),{colorList[code[index+1]]})"
            rects.append(a)
            index += 1

    for rect in rects:
       exec(rect)
    end_drawing()
    index += 1


close_window()