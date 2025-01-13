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

vol_tick = 0


while not window_should_close():
    begin_drawing()
    
    if not is_sound_playing(sand):
        play_sound(sand)
    vol = m.sin(vol_tick/2)+.5
    set_sound_volume(sand,vol)
    draw_texture_ex(bed,Vector2(10,10),0,10,WHITE)
    draw_text(f"{round(vol,2)}",100,100,20,PURPLE)
    vol_tick += .1
    end_drawing()
close_audio_device()
close_window()
