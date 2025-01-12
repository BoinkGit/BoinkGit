from pyray import *
import os

for root,dir,files in os.walk(get_working_directory()):
    print(root)


"""
init_window(500,500,"paralyzed gunman in a dystopian hospital")

set_target_fps(60)

close_window()

while not window_should_close():
    begin_drawing()
    play_sound()
    
    end_drawing()
close_window()
"""