from pyray import *

mouse_upgrades = []
commands = ["move", "right", "left"]

class catcher:
    pass

class scaredy:
    pass

class cat:
    pass

level = -1


init_window(750,500,"Mouse Engineer: A Robbers Dystopia")

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    mx = get_mouse_x()
    my = get_mouse_y()
    mshake = get_mouse_delta

    draw_circle_v(Vector2(mx,my),10,BROWN)
    



    end_drawing()