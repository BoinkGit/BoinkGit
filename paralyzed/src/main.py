from pyray import *
import os
import math as m

for root in os.walk(get_working_directory()):
    try:
        path = f"{root[0]}\\{root[1][root[1].index('paralyzed')]}"
        break
    except:
        raise FileExistsError("please dont change the name of the folder. that like, REALLY breaks it.")
change_directory(path)


init_window(500,500,"paralyzed gunman in a dystopian hospital")
init_audio_device()
set_target_fps(60)

sand = load_sound(os.path.join(path,"assets","epic_sand.wav"))
bed = load_texture(os.path.join(path,"assets","bed.png"))

## FUNCTIONS
def normal_angle(x1,y1,x2,y2,dist):
    dx = x2-x1; dy = y2-y1
    if dx == 0:
        if dy > 0:
            dy = dist
        else: dy = -1*dist
    else:
        angle = m.atan(dy/dx)
        dx = int(m.cos(angle)*dist)
        dy = int(m.sin(angle)*dist)
    if x2 < x1:
        dx *= -1; dy *= -1
    return (dx,dy)



## CLASSES
class player:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        print(self)
    def set_extras(self,friction,gravity):
        self.friction = friction
        self.gravity = gravity
    def set_controls(self,up,down,left,right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
    def shoot(self):
        direction = normal_angle(self.x,self.y,get_mouse_x(),get_mouse_y(),1)
        return bullet(self,direction[0],direction[1],0,0,'big')

    def draw(self,w,h,texture=None):
        w = int(w)
        h = int(h)
        if texture == None:
            draw_rectangle(self.x-w//2,self.y-h//2,w,h,RED)
        else: 
            print("bruh i didnt add yet wait more")
            quit()
    def move(self,speed=1):
        self.vy -= (is_key_down(self.up)-is_key_down(self.down))*speed
        self.vx += (is_key_down(self.right)-is_key_down(self.left))*speed
        self.vy *= self.friction
        self.vx *= self.friction
        self.y += int(self.vy)
        self.x += int(self.vx)


class bullet:
    def __init__(self,player,x,y,vx,vy,type):
        self.player = player
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type
    def draw(self):
        draw_circle(self.x,self.y,3,ORANGE)

c = player(0,0,92,0)
c.set_controls(KEY_W,KEY_S,KEY_A,KEY_D)
c.set_extras(.8,0)
b = c.shoot()

# dang that works?!
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    c.draw(20,20)
    c.move()
    if is_mouse_button_pressed(0):
        b = c.shoot()
    b.draw()
    
    

    end_drawing()
close_audio_device()
close_window()
