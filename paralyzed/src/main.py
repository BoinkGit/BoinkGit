from pyray import *
import os
import math as m

for root, a, b in os.walk(get_working_directory()):
    try:
         if root.endswith("\\paralyzed"):
            path = root
    except:
        raise FileExistsError("please dont change the name of the folder. that like, REALLY breaks it.")
change_directory(path)


init_window(500,500,"paralyzed gunman in a dystopian hospital")
init_audio_device()
set_target_fps(60)

sand = load_sound(os.path.join(path,"assets","epic_sand.wav"))
bed = load_texture(os.path.join(path,"assets","bed.png"))

class player:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        print(self)
    def shoot(self):
        return bullet(self,0,0,0,0,'big')

class bullet:
    def __init__(self,player,x,y,vx,vy,type):
        self.player = player
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type

c = player(0,0,92,0)

d = c.shoot()

print(d.player.vx)
# dang that works?!
while not window_should_close():
    begin_drawing()
    
    
    

    end_drawing()
close_audio_device()
close_window()
