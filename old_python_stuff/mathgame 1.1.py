# 1.0: adds math part, difficulty screen, exit
# 1.1: fixes quit and div0 errors, allows you to return to menu, gamemodes normal and single,
# multiplication isn't too high, division is all integers, stops showing pop-ups for some reason.
import pyautogui as pyag
from random import randint
problem = ''
c = 'woah'
fc1 = ''
fc2 = ''
choosable = [c,fc1,fc2]
answers = []
pts = 0
difficulty = 0
def math(diff,opt):
    global problem, c, fc1 ,fc2
    a = randint(diff*(1-diff),diff*(9+diff))
    b = randint(diff*(1-diff),diff*(9+diff))
    c = 'NAN'
    if opt == diff:
        r = diff
    else: r = randint(opt,diff)
    if r == 1:
        problem = str(a)+' + '+str(b)+' = ?'
        c = a + b
        fc1 = a + b + randint(-6,-2)
        fc2 = a + b + randint(2, 4)
    elif r == 2:
        problem = str(a)+' - '+str(b)+' = ?'
        c = a - b
        fc1 = a - b + randint(-6,-2)
        fc2 = a - b + randint(2, 4)
    elif r == 3:
        a = int(round(a/diff))
        b = int(round(b/diff))
        problem = str(a)+' * '+str(b)+' = ?'
        c = a * b
        fc1 = a * b/ + randint(-6,-2)
        fc2 = a * (b + randint(-2, 2))
    elif r == 4:
        if b == 0:
            b = 1000
        if '.' in str(a/b):
            if str(a/b)[-1] != '0':
                while a % b != 0:
                    b = randint(diff*(1-diff),diff*(9+diff))
                    if str(b) in '0-1':
                        b = 1000
        problem = str(a)+' / '+str(b)+' = ?'
        c = int(a / b)
        fc1 = int(a / b + randint(-6,-2))
        r = randint(-2,2)
        if b + r == 0:
            b += 2*randint(0,1)-1
        else: b + r
        fc2 = int(round(a / b))
        
def choose():
    global answers, choosable
    answers = []
    choosable = [c,fc1,fc2]
    for i in range(3):
        r = randint(0,len(choosable)-1)
        answers.append(str(choosable[r]))
        choosable.remove(choosable[r])
    answers.append('menu')

def ask():
    global s, pts
    s = pyag.confirm(text=problem,title='MATH GAME! points:'+str(pts),buttons=answers)
    if  s == str(c):
        pyag.alert(text='Good Job! '+str(c)+' is the correct answer!',title='Nice!',button='Hooray')
        pts += 1
    elif s == 'menu':
        pass
    else: pyag.alert(text='Too Bad. '+str(c)+' was the correct answer',title='womp womp',button='D:')

def easyAll(diff,opt):
    math(diff,opt)
    choose()
    ask()
while True:
    pts = 0
    if type(difficulty) == type(None):
        break
    gamemode = pyag.confirm(text='Choose a gamemode:',title='GAMES',buttons=['normal','single','exit'])
    if gamemode == 'exit':
        pyag.alert(text='Play again soon!',title='goodbye',button='Exit')
        break
    if gamemode == 'normal':
        difficulty = pyag.confirm(text='Choose a difficulty:',title='DIFFICULTY',buttons=['1','2','3','4','menu'])
        gamemode = 1
    if gamemode == 'single':
        difficulty = pyag.confirm(text='1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division',title='DIFFICULTY',buttons=['1','2','3','4','menu'])
        if type(difficulty) == type(None):
            break
        if difficulty != 'menu':
            difficulty = int(difficulty)
            gamemode = difficulty
    if type(gamemode) == type(None):
        break
    while True:
        if difficulty == 'menu':
            break
        elif type(difficulty) == type(None):
            break
        else: difficulty = int(difficulty)
        easyAll(difficulty,gamemode)
        if s == 'menu':
            break
