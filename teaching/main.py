from pyray import *
from random import randint

def rand(min,max):
    return randint(min,max)


numlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
mines = []
for i in range(16):
    mines.append(f"{rand(0,9)}{numlet[rand(0,9)]}")
clicks = {}

def grid(x,y):
    return f"{x}{numlet[y]}"
def ungrid(grid):
    return int(grid[0]), numlet.index(grid[1])

init_window(500,500,"window name")


while not window_should_close():
    rmx = get_mouse_x(); rmy = get_mouse_y()
    mx, my = rmx // 50, rmy // 50

    begin_drawing()
    clear_background(DARKGRAY)

    for i in range(10):
        for j in range(10):
            draw_rectangle(i*50+3,j*50+3,44,44,GRAY)
            draw_pos = grid(i,j)

            #if draw_pos in mines:
            #    draw_rectangle(i*50+3,j*50+3,44,44,BLUE)

            if draw_pos in clicks:
                if clicks[draw_pos] == -1:
                    draw_rectangle(i*50+15,j*50+15,20,20,RED)
                if clicks[draw_pos] == "*":
                    draw_rectangle(i*50+10,j*50+10,30,30,BLACK)
                if clicks[draw_pos] in range(0,8):
                    draw_text(f"{clicks[draw_pos]}",i*50+13,j*50+2,50,WHITE)
            
            




    #draw_rectangle(mx*50+1,my*50+1,48,48,ORANGE)

    if is_mouse_button_pressed(1):
        pos = grid(mx,my)
        if pos in clicks:
            if clicks[pos] == -1:
                clicks.pop(pos)
        else:
            clicks[pos] = -1

    def check(x,y):
        near_mines = 0
        for i in range(0,8):
            if x+(i%3)-1 in range(10) and y+(i//3)-1 in range(10):
                if grid(x+(i%3)-1,y+(i//3)-1) in mines:
                   near_mines += 1
        if not grid(x,y) in mines:
            return near_mines
    if is_mouse_button_pressed(0):
        pos = grid(mx,my)
        if not pos in clicks:
            if pos in mines:
                clicks[pos] = "*"
            else:
                if check(mx,my) == 0:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if mx+i in range(10) and my+j in range(10):
                                pos = grid(mx+i,my+j)
                                clicks[pos] = check(mx+i,my+j)
                else:
                    clicks[pos] = check(mx,my)

                        
                
            



        


    end_drawing()
close_window()


