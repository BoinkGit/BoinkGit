from keyboard import send
from mouse import click, move
from time import sleep
def keys(moves):
    i = 0
    sleep(0.1)
    while i < len(moves):
        if moves[i] == 's':
            send('space')
        elif moves[i] == 'r':
            send('right')
        elif moves[i] == 'l':
            send('left')
        elif moves[i] == 'u':
            send('up')
        elif moves[i] == 'd':
            send('down')
        sleep(0.1)
        i += 1
move(0,0)
click('left')
sleep(0.1)
move(1000,450)
click('left')
sleep
move(400,200)
sleep(0.1)
click('left')
keys('srsrrrrus')
