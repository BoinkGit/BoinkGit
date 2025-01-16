import time

# pen class

class pen:
    def __init__(self):
        pass
    def reset(self): 
        grid = []
        for y in range(HEIGHT):
            grid.append([0]*WIDTH)
        
    def pathfind(self,x1,y1,x2,y2):
        global grid

        # first we set point to(x1,y1)

        pos_x = x1
        pos_y = y1

        grid[pos_y][pos_x] = 1

        # keep distance all squared

        while pos_x != x2 or pos_y != y2:
            for row in grid:
                print(row)

            time.sleep(0.5)

            dst_list = []
            min_dst_dir = []

            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    current_dst = (x2 - (pos_x+dx))**2 + (y2 - (pos_y+dy))**2
                    dst_list.append(current_dst)
                    if current_dst == min(dst_list):
                        min_dst_dir = [dx,dy]

            pos_x += min_dst_dir[0]
            pos_y += min_dst_dir[1]
            grid[pos_y][pos_x] = 1
    def draw_line(self, x1, y1, x2, y2):
        dy = (y2-y1)
        dx = (x2-x1)
        dst = ((dx)^2 + (dy)^2)**(1/2)

        step_y = dy/(dst*5)
        step_x = dx/(dst*5)
        pos_x = x1
        pos_y = y1
        while pos_x < x2 and pos_y < y2:
            grid[round(pos_y)][round(pos_x)] = 'X'
            pos_x += step_x
            pos_y += step_y

        
        
        # y = slope * (x-x1) + y1


        

WIDTH = 20
HEIGHT = 20

# MAIN #

grid = []
for y in range(HEIGHT):
    grid.append(['_']*WIDTH)

line = pen()

line.draw_line(0,0,12,19)

for row in grid:
    print(row)
