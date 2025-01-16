import turtle, time
class sprite():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def move(self,dx=0,dy=0):
        self.x += dx
        self.y += dy
    def draw(self,dir=["m10","t90","m10","t90","m10","t90","m10"]):
            turtle.clearscreen(); turtle.pu()
            turtle.goto(self.x, self.y); turtle.setheading(0)
            turtle.pd()
            for i in range(len(dir)):
                if dir[i][0] == "m":
                    turtle.fd(int(
                         dir[i][1:len(dir[i])]
                         ))
                if dir[i][0] == "t":
                    turtle.rt(int(
                          dir[i][1:len(dir[i])]
                          ))
            turtle.pu()

player = sprite()
for i in range(10):
     player.draw()
     player.move(dx = 10)
     time.sleep(0.25)
    

