from pyray import *
from os.path import join as os

file = "load_white.cb"  #input("File Name: ")
if file.endswith(".cb"):
    longcode = open(os("code_byte","programs",f"{file}"),"r").read()
else: 
    print("Must be type .cb file")
    raise FileNotFoundError("Must be type .cb file")

longcode = longcode.split()
code = []
for word in longcode:
    for letter in word:
        if letter in "01234567":
            code.append(letter)

for i in range(len(code)):
    code[i] = int(code[i])
    """if not code[i] in range(8):
        raise ValueError("Values out of range 0-7")"""

bytVar = [0,0,0,0,0,0,0,0]
intVar = [0,0,0,0,0,0,0,0]
flags = {}
loops = 0

colorList = [BLACK,WHITE, RED,GREEN,DARKBLUE, YELLOW,VIOLET,SKYBLUE]
pointer = Vector2(0,0)

rects = {}

index = 0

init_window(512,512,"Fantasy Console")

#set_target_fps(60)

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    if index < len(code):
        num = code[index]

# SET POINTER POSITION
        if num == 0:
            if code[index+1] == 0:
                pointer.x = eval(f"0o{code[index+2]}{code[index+3]}")*8
                pointer.y = eval(f"0o{code[index+4]}{code[index+5]}")*8
            elif code[index+1] == 1:
                pointer.x += eval(f"0o{code[index+3]}")*[8,-8][code[index+2]]
                pointer.y += eval(f"0o{code[index+5]}")*[8,-8][code[index+4]]
            elif code[index+1] == 2:
                pointer.x = int(f"{intVar[code[index+3]]}",8)*8
                pointer.y = int(f"{intVar[code[index+5]]}",8)*8
            elif code[index+1] == 3:
                pointer.x = intVar[code[index+3]][1]*[8,-8][intVar[code[index+3]][0]]
                pointer.y = intVar[code[index+5]][1]*[8,-8][intVar[code[index+5]][0]]
                pass
            
            index += 5

# SET COLOR
        elif num == 1:
            rects[f"({pointer.x}, {pointer.y})"] = colorList[code[index+1]]
            index += 1

# SET VARIABLE BYTE
        elif num == 2:
            if code[index+2] == 0:
                bytVar[code[index+1]] = code[index+3]
            elif code[index+2] == 1:
                bytVar[code[index+1]] = bytVar[code[index+3]]
            elif code[index+2] == 2:
                bytVar[code[index+1]] = (int(f"0o{intVar[code[index+3]]}",8) % 8)
            elif code[index+2] == 3:
                bytVar[code[index+1]] = colorList.index(rects[f"({pointer.x}, {pointer.y})"])

            index += 3

# SET VARIABLE INTEGER
        elif num == 3:
            if code[index+2] == 0:
                intVar[code[index+1]] = int(f"{code[index+3]}{code[index+4]}")
            elif code[index+2] == 1:
                intVar[code[index+1]] = bytVar[code[index+4]]
            elif code[index+2] == 2:
                intVar[code[index+1]] = intVar[code[index+4]]
            elif code[index+2] == 3:
                intVar[code[index+1]] = colorList.index(rects[f"({pointer.x}, {pointer.y})"])
            elif code[index+2] == 4:
                intVar[code[index+1]] = int(oct(int(pointer.x // 8)).removeprefix("0o"))
            elif code[index+2] == 5:
                intVar[code[index+1]] = int(oct(int(pointer.y // 8)).removeprefix("0o"))
            
            index += 4

# MATH VARIABLE INTEGER
        elif num == 4:
            intVar[code[index+1]] = int(f"{intVar[code[index+1]]}",8)

            if code[index+3] == 0:
                value = int(f"{code[index+4]}{code[index+5]}",8)
            elif code[index+3] == 1:
                value = intVar[int(f"{code[index+5]}",8)]

            if code[index+2] == 0: # +=
                intVar[code[index+1]] += value
            elif code[index+2] == 1: # -=
                intVar[code[index+1]] -= value
            elif code[index+2] == 2: # *=
                intVar[code[index+1]] *= value
            elif code[index+2] == 3: # /=
                if value == 0:
                    intVar[code[index+1]] = 0
                else: intVar[code[index+1]] //= value

            intVar[code[index+1]] = int(oct(intVar[code[index+1]] % 64).removeprefix("0o"))
            index += 5
# SET FLAG
        elif num == 7:
            if code[index+1] == 0:
                flags[f"{code[index+2]}"] = index - 1
            elif code[index+1] == 1:
                index = flags[f"{code[index+2]}"] - 2
                loops += 1
            index += 2

# DRAW SCREEN
    for rect in rects:
       draw_rectangle(int(eval(rect)[0]),int(eval(rect)[1]),8,8,rects[rect])
    draw_circle_v(pointer,2,ORANGE)
    draw_text(f"bytVar: {bytVar}",0,470,20,WHITE)
    draw_text(f"intVar: {intVar}",0,490,20,WHITE)
    end_drawing()

# OTHER
    index += 1


close_window()