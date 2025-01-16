'''def base(n, b):
    if b > 36: raise ValueError('base should be from 2-36')
    if b < 2: raise ValueError('base should be from 2-36')
    chars = ['0','1','2','3','4','5','6','7','8',
             '9','A','B','C','D','E','F','G','H',
             'I','J','K','L','M','N','O','P','Q',
             'R','S','T','U','V','W','X','Y','Z']
    if n == 0:
        return [0]
    digits = []; num = []
    while n:
        digits.append(int(n % b))
        n //= b
    for i in digits[::-1]:
        num.append(chars[i])
    return ''.join(num)
print(base(16777215,1))'''
import turtle
turtle.colormode(255)
class sprite:
    def __init__(s,pixels):
        s.pixels = pixels
    def draw(s,x,y):
        turtle.pu(); turtle.goto(x,y); turtle.pensize(10)
        for dx in range(5):
            if s.pixels[dx] != None:
                turtle.pencolor(s.pixels[dx])
                turtle.pd()
            else: turtle.
            turtle.goto(x+dx*10,y)
shape = sprite([None,(255,0,0),None,(255,0,0),(0,255,255)])
shape.draw(0,0)
turtle.exitonclick()